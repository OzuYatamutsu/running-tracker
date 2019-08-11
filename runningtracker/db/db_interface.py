from sqlite3 import connect, Connection
from pathlib import Path
SCHEMA_VERSION = 'v1'
SCHEMA_LOCATION = str(
    Path('.').parent.parent.joinpath(
        'database', f"schema_{SCHEMA_VERSION}.sql"
    )
)
DATABASE_NAME = 'runningtracker.db'


def _init_db(conn: Connection) -> None:
    """
    Runs the schema DDL to initialize the database.
    """

    ddl = ""
    with open(SCHEMA_LOCATION) as f:
        ddl = f.read()

    conn.cursor().executescript(ddl)


def _row_factory(cursor, row) -> dict:
    """
    (Passed into SQLite to return a resultset
    as a list of dicts)
    """

    result = {}
    for index, column in enumerate(cursor.description):
        result[column[0]] = row[index]
    return result


def _get_db() -> Connection:
    """
    Returns a db connection object.
    """

    db_needs_initing = not Path(DATABASE_NAME).exists()
    conn = connect(DATABASE_NAME)
    conn.row_factory = _row_factory

    if db_needs_initing:
        _init_db(conn)
    return conn
