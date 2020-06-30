from app import create_app
from config import config
import os
from flask import request, jsonify
from app.models.link import Link
from app.exceptions.model_not_found import ModelNotFoundError
from marshmallow import Schema, fields

from app.requests.link_create_requests import link_create_requests
from marshmallow import (
    ValidationError
)

app = create_app(config['development'])


class LinkSchema(Schema):
    shortened_url = fields.Function(lambda obj: obj.shortener_url())

    class Meta:
        fields = ('original_url', 'code', 'shortened_url', 'requested_count')


def response(data):
    return jsonify({
        'data':  data
    })


@app.route('/')
def hello():
    try:
        link = Link.get_by(code=request.args.get('code', ''))
    except ModelNotFoundError as e:
        return jsonify({'error': str(e)}), 404

    link.increment('requested_count')

    link.save()

    return response(LinkSchema().dump(link)), 200


@app.route('/', methods=['POST'])
def store():
    json = request.get_json(force=True)

    try:
        link_create_requests.load(json)
    except ValidationError as err:
        return err.messages, 422

    link = Link.get_or_create(original_url=json['url'])

    link.code = link.get_code()

    link.save()

    return response(LinkSchema().dump(link)), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
