from app import create_app
from config import config
import os
from flask import request, jsonify
from app.models.link import Link
from app.exceptions.model_not_found import ModelNotFoundError

from app.requests.link_create_requests import link_create_requests
from marshmallow import (
    ValidationError
)
from app.models import db

app = create_app(config['development'])


@app.route('/')
def hello():
    try:
        link = Link.get_by(code=request.args.get('code', ''))

        return jsonify({
            'data':  link.serialize()
        }), 200
    except ModelNotFoundError as e:
        return jsonify({'error': str(e)}), 404


@app.route('/', methods=['POST'])
def store():
    json = request.get_json(force=True)

    try:
        link_create_requests.load(json)
    except ValidationError as err:
        return err.messages, 422

    link = Link(original_url=json['url'])

    db.session.add(link)
    # link.code = link.get_code()

    # link.save()

    return jsonify({
        'data': {
            'id': link.id
        }
    }), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
