import csv

import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base
from model import Company

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
    "input_file", type=click.File(encoding="utf-8"), metavar="CSV")
def main(database, domain, input_file):
    engine = create_engine('sqlite:///' + database)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    with input_file:
        for row in read_csv(input_file):
            insert_company(
                session=session,
                name=row['company name'],
                revenue=row['revenue'],
                origin=input_file.name,
                domain=domain,
            )
    session.commit()


if __name__ == "__main__":
    main()
