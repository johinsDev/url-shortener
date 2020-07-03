from flask_restful import abort
from functools import wraps


def binding(model):
    def inner(function):
        @wraps(function)
        def wrap(*args, **kwargs):
            try:
                values = dict()

                values[str(model.__name__).lower()] = model.get_by(**kwargs)

                return function(*args, **values, **kwargs)
            except:
                return abort(404, message="Model {} doesn't exist".format(model.__name__))

        return wrap

    return inner
