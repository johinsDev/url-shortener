from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length, URL


class CreateLinkValidationSchema(Schema):
    url = fields.Str(
        required=True,
        validate=[URL(error='Hmm, that doesn\'t look like a valid URL.')],
        error_messages={
            'required': 'Please enter a URL to shorten.',
        }
    )
