from snowflake.snowpark import Session
from config import SNOWFLAKE


def get_session():
    return Session.builder.configs(SNOWFLAKE).create()


def run_sql(query: str):
    session = get_session()

    try:

        rows = session.sql(query).collect()

        # Convert Snowpark Row -> dict
        return [row.as_dict() for row in rows]

    finally:
        session.close()