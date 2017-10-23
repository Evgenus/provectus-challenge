from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):

    __tablename__ = 'companies_revenue'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    revenue = Column(Numeric(16, 2), nullable=True)
    revenue_raw = Column(String, nullable=True)
    added_at = Column(DateTime, default=datetime.now)
    domain = Column(String, nullable=False)
    origin = Column(String, nullable=False)
