from marshmallow import Schema, fields


class LinkSchema(Schema):
    shortened_url = fields.Function(lambda obj: obj.shortener_url)
    original_url = fields.Str()
    code = fields.Str()
