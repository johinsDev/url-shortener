from flask_restful import Resource, abort
from .model import Link
from flask import request
from datetime import datetime
from .schema_response import LinkSchema
from .decorators.parser_url import modify_url_request_data
from app.exceptions.model_not_found import ModelNotFoundError


class LinkResource(Resource):
    def get(self):
        try:
            link = Link.get_by(code=request.args.get('code'))
        except ModelNotFoundError as e:
            abort(404, message=str(e))

        link.last_used = datetime.utcnow()

        link.increment('used_count')

        link.save()

        return LinkSchema().dump(link)

    @modify_url_request_data
    def post(self, url):
        link = Link.get_or_create(original_url=url)

        link.increment('requested_count')

        link.last_requested = datetime.utcnow()

        link.save()

        return LinkSchema().dump(link)
