from marshmallow import Schema, fields


class LinkSchema(Schema):
    shortened_url = fields.Function(lambda obj: obj.shortener_url)

    class Meta:
        fields = ('original_url', 'code', 'shortened_url')
