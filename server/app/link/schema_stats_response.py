from marshmallow import fields
from .schema_response import LinkSchema


class LinkStatsSchema(LinkSchema):
    requested_count = fields.Integer()
    used_count = fields.Integer()
    last_used = fields.DateTime()
    last_requested = fields.DateTime()
