from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from runningtracker.db.models.datapoint import Datapoint
from sqlite3 import connect, Connection
from typing import Type, List
from pathlib import Path


SCHEMA_VERSION = 'v2'
SCHEMA_LOCATION = str(
    Path('.').parent.parent.joinpath(
        'database', f"schema_{SCHEMA_VERSION}.sql"
    )
)
DATABASE_NAME = 'runningtracker.db'


def commit(datapoint: Datapoint) -> None:
    """
    Commits a datapoint to the database.
    """

    with get_db() as db:
        db.cursor().execute(
            datapoint.COMMIT_SQL, datapoint.to_sql_params()
        )


def get_last_n_datapoints(data_type: Type[Datapoint], n=1) -> List[Datapoint]:
    """
    Returns the last n most recent datapoints of the given type.
    """

    with get_db() as db:
        cursor = db.cursor()

        cursor.execute(
            f"SELECT * FROM {data_type.TABLE_NAME} "
            "ORDER BY entry_id DESC LIMIT ?", (n,)
        )

        return [
            data_type(**row) for row in cursor.fetchall()
        ]


def get_vitals_datapoint_by_id(entry_id: int) -> VitalsDatapoint:
    """
    Fetches a VitalsDatapoint object from the database.
    If none were found by the ID, raises ValueError.
    """

    with get_db() as db:
        cursor = db.cursor()

        cursor.execute(
            f"SELECT * FROM {VitalsDatapoint.TABLE_NAME} "
            f"WHERE entry_id = ?", (entry_id,)
        )

        try:
            return VitalsDatapoint(**cursor.fetchone())
        except TypeError:
            raise ValueError(
                f"Could not find a vitals datapoint with entry_id={entry_id}."
            )


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


def get_db() -> Connection:
    """
    Returns a db connection object.
    """

    db_needs_initing = not Path(DATABASE_NAME).exists()
    conn = connect(DATABASE_NAME)
    conn.row_factory = _row_factory

    if db_needs_initing:
        _init_db(conn)
    return conn
