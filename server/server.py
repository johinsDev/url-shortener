from app import create_app, cache
from config import config
import os
from flask import request, jsonify
from app.models.link import Link
from app.exceptions.model_not_found import ModelNotFoundError
from marshmallow import Schema, fields
from app.requests.link_create_requests import link_create_requests
from functools import wraps
from marshmallow import (
    ValidationError
)

app = create_app(config['development'])


def modify_url_request_data(function):
    def wrap(*args, **kwargs):
        json = request.get_json(force=True)

        try:
            link_create_requests.load({"url": json['url']})
        except:
            request.url = "aja"
            return function('http://' + json['url'])

        return function(json['url'])

    wrap.__name__ = function.__name__

    return wrap


class LinkSchema(Schema):
    shortened_url = fields.Function(lambda obj: obj.shortener_url())

    class Meta:
        fields = ('original_url', 'code', 'shortened_url', 'requested_count')


def response(data):
    return jsonify({
        'data':  data
    })

# @TODO CAche forever, use flask resource, divider better files, decorator for validate


@app.route('/')
def hello():
    try:
        key = "link." + request.args.get('code', '')

        link = cache.get(key)

        if link is None:
            link = Link.get_by(code=request.args.get('code', ''))

            cache.add("link." + request.args.get('code', ''), link, 500000000)
    except ModelNotFoundError as e:
        return jsonify({'error': str(e)}), 404

    link.increment('requested_count')

    link.save()

    return response(LinkSchema().dump(link)), 200


def binding(model):
    def inner(function):
        @wraps(function)
        def wrap(*args, **kwargs):
            try:
                values = dict()

                values[str(model.__name__).lower()] = model.get_by(**kwargs)

                return function(*args, **values, **kwargs)
            except ModelNotFoundError as e:
                return jsonify({'error': str(e)}), 404

        return wrap

    return inner


@app.route('/model_binding/<code>')
@binding(Link)
def model_binding(code, link):
    return response(LinkSchema().dump(link)), 200


@app.route('/', methods=['POST'])
@modify_url_request_data
def store(url):
    link = Link.get_or_create(original_url=url)

    link.code = link.get_code()

    link.save()

    return response(LinkSchema().dump(link)), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
