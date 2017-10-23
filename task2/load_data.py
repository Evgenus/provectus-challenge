import csv
from datetime import datetime

import click
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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


def read_csv(stream):
    reader = csv.DictReader(stream)
    for row in reader:
        yield row


def insert_company(session, name, revenue, domain, origin):
    company = Company(
        name=name,
        #revenue=parse_revenue_using_currency_and_rate(revenue),
        revenue_raw=revenue,
        domain=domain,
        origin=origin,
    )
    session.add(company)


@click.command(
    short_help="load data from CSV into sqlite")
@click.option(
    "--database", type=str, default="db.sqlite")
@click.option(
    "--domain", type=str, required=True, help="customer name or CRM url")
@click.argument(
    "input", type=click.File(encoding="utf-8"), metavar="CSV")
def main(database, domain, input):
    engine = create_engine('sqlite:///' + database)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    with input:
        for row in read_csv(input):
            insert_company(
                session=session,
                name=row['company name'],
                revenue=row['revenue'],
                origin=input.name,
                domain=domain,
            )
    session.commit()


if __name__ == "__main__":
    main()
