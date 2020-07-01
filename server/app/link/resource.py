from flask_restful import Resource
from flask import request
from ..models.link import Link
from .schema_response import LinkSchema

# @TODO Validation with marshalle


class LinkResource(Resource):
    def post(self):
        data = request.get_json()

        link = Link.get_or_create(original_url=data['url'])

        # @TODO add observer for this
        link.code = link.get_code()

        link.save()

        # @TODO Pattern adapter with interface for validation
        return LinkSchema().dump(link)
