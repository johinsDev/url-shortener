import sqlalchemy as sa
import os
from app import db
from ..exceptions.code_generation_exception import CodeGenerationException
from ..helpers.Math import Math
from datetime import datetime

from ..mixins.base import Base


class Link(db.Model, Base):
    __tablename__ = 'links'

    __hidden__ = []

    id = sa.Column(sa.BigInteger, primary_key=True)
    original_url = sa.Column(sa.Text, unique=True, nullable=False)
    code = sa.Column(sa.Text, unique=True, nullable=True)
    requested_count = sa.Column(
        sa.BigInteger,  server_default="0", nullable=False)
    used_count = sa.Column(sa.BigInteger,  server_default="0", nullable=False)

    def get_code(self):
        if self.id is None:
            raise CodeGenerationException

        return Math.encode_id(self.id)

    @property
    def shortener_url(self):
        if self.code is None:
            return None

        return f'{os.getenv("CLIENT_URL")}/{self.code}'

    def __repr__(self):
        return '<Link %r>' % self.id
