from runningtracker.db.models.datapoint import Datapoint
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vo2Datapoint(Datapoint):
    """
    Describes metadata relating to a Cooper test measurement,
    used to calculate an approximation of VO2max.
    """

    timestamp: datetime
    duration_min: int
    duration_sec: int
    notes: str

    COMMIT_SQL = (
        "INSERT INTO vo2 (timestamp, duration_min, duration_sec, "
        "notes) VALUES (?, ?, ?, ?, ?, ?)"
    )

    def to_sql_params(self) -> tuple:
        """
        Casts this object into a tuple in the order described above.
        (It will be ready to be inserted into a parameterized query.)
        """

        return (
            self.timestamp, self.duration_min, self.duration_sec,
            self.notes
        )
