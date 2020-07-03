from flask import request
from functools import wraps

from .. import validation_schema


def modify_url_request_data(function):
    def wrap(*args, **kwargs):
        json = request.get_json(force=True)

        try:
            validation_schema.CreateLinkValidationSchema().load(
                {"url": json['url']})
        except:
            return function(url='http://' + json['url'], *args, **kwargs)

        return function(json['url'])

    wrap.__name__ = function.__name__

    return wrap
