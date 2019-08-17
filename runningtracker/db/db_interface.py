from runningtracker.db.models.activity_datapoint import ActivityDatapoint
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

    with _get_db() as db:
        db.cursor().execute(
            datapoint.COMMIT_SQL, datapoint.to_sql_params()
        )


def get_last_n_datapoints(data_type: Type[Datapoint], n=1) -> List[Datapoint]:
    """
    Returns the last n most recent datapoints of the given type.
    """

    with _get_db() as db:
        cursor = db.cursor()

        assert data_type in [VitalsDatapoint, ActivityDatapoint],\
            "Unsupported data type."

        cursor.execute(
            f"SELECT * FROM {VitalsDatapoint.TABLE_NAME} "
            "ORDER BY measured_on LIMIT ?", (n,)
        )

        vitals_datapoints = [
            VitalsDatapoint(**row) for row in cursor.fetchall()
        ]

        if data_type is VitalsDatapoint:
            return vitals_datapoints
        elif not vitals_datapoints:
            # We wanted activity datapoints, but we won't find any.
            return []

        # Otherwise, we want activity datapoints
        cursor.execute(
            f"SELECT * FROM {ActivityDatapoint.TABLE_NAME} "
            "ORDER BY measured_on LIMIT ?", (n,)
        )

        activity_datapoints = []
        for row in cursor.fetchall():
            # Resolve ID of vitals entry pointed to by activity entry
            linked_to_vitals = [
                vitals_datapoint for vitals_datapoint in vitals_datapoints
                if vitals_datapoint.entry_id == row.pop(
                    'linked_to_vitals_entry', None
                )
            ][0]

            # Link the objects together
            assert not not linked_to_vitals
            row['linked_to_vitals_entry'] = linked_to_vitals

            # Construct the object
            activity_datapoints.append(ActivityDatapoint(**row))
        return activity_datapoints


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
