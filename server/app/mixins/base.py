import sqlalchemy as sa

from ..exceptions.model_not_found import ModelNotFoundError
from .utils import classproperty
from .timestamp import Timestamp
from ..models import db


class Base(Timestamp):
    @classproperty
    def columns(cls):
        return sa.inspect(cls).columns.keys()

    @classmethod
    def query(cls):
        return db.session.query(cls)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def first(cls):
        return cls.query.first()

    @classmethod
    def find(cls, id_):
        return cls.query.get(id_)

    @classmethod
    def create(cls, **kw):
        r = cls(**kw)
        db.session.add(r)
        return r

    @classmethod
    def find_or_fail(cls, id_):
        result = cls.find(id_)
        if result:
            return result
        else:
            raise ModelNotFoundError("{} with id '{}' was not found"
                                     .format(cls.__name__, id_))

    @classmethod
    def get_by(cls, **kw):
        result = cls.query.filter_by(**kw).first()

        if result:
            return result
        else:
            raise ModelNotFoundError("Error")

    def save(self):
        db.session.add(self)

    def serialize(self):
        result = dict()
        for key in self.columns:
            if key not in self.__hidden__:
                result[key] = getattr(self, key)

        return result
