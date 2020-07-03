from marshmallow import fields
from .schema_response import LinkSchema


class LinkStatsSchema(LinkSchema):
    requested_count = fields.Integer()
    used_count = fields.Integer()
