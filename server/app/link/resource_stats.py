from flask_restful import Resource, abort
from .model import Link
from app import cache
from flask import request
from .schema_stats_response import LinkStatsSchema
from app.exceptions.model_not_found import ModelNotFoundError

TIME = 10 * 60


class LinkStatsResource(Resource):
    def get(self):
        try:
            @cache.cached(timeout=TIME, key_prefix="stats." + request.args.get('code', ''))
            def get_link():
                return Link.get_by(code=request.args.get('code'))

            link = get_link()
        except ModelNotFoundError as e:
            abort(404, message=str(e))

        return LinkStatsSchema().dump(link)
