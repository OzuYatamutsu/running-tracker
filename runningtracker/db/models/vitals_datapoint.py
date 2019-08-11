from runningtracker.db.models.datapoint import Datapoint
from dataclasses import dataclass
from datetime import datetime


@dataclass
class VitalsDatapoint(Datapoint):
    """
    Describes a measurement of vital statistics at
    a specific time.
    """

    timestamp: datetime
    weight_lb: float
    bp_systolic: float
    bp_diastolic: float
    heart_bpm: int
    notes: str

    TABLE_NAME = "vitals"

    COMMIT_SQL = (
        f"INSERT INTO {TABLE_NAME} (timestamp, weight_lb, bp_systolic, "
        "bp_diastolic, heart_bpm, notes) VALUES "
        "(?, ?, ?, ?, ?, ?)"
    )

    def to_sql_params(self) -> tuple:
        """
        Casts this object into a tuple in the order described above.
        (It will be ready to be inserted into a parameterized query.)
        """

        return (
            self.timestamp, self.weight_lb, self.bp_systolic,
            self.bp_diastolic, self.heart_bpm, self.notes
        )
