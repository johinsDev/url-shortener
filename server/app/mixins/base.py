import sqlalchemy as sa
from app import db
from sqlalchemy_utils import Timestamp


class Base(Timestamp):
    @classmethod
    def get_or_create(cls, **kw):
        r = cls.get_by(**kw)

        if not r:
            r = cls(**kw)
            db.session.add(r)
            db.session.flush()

        return r

    @classmethod
    def get_by(cls, **kw):
        return cls.query.filter_by(**kw).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def increment(self, column):
        setattr(self, column, getattr(self, column) + 1)
        return self
