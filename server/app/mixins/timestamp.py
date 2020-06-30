from datetime import datetime
from sqlalchemy import Column,  DateTime, func


class Timestamp(object):
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=datetime.now)
