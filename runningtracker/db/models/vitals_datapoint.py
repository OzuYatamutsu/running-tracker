from runningtracker.db.models.datapoint import Datapoint
from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class VitalsDatapoint(Datapoint):
    """
    Describes a measurement of vital statistics at
    a specific time.
    """

    # Assigned at insertion.
    entry_id: Optional[int]
    measured_on: date
    weight_lb: float
    bp_systolic: float
    bp_diastolic: float
    heart_bpm: int
    notes: str

    TABLE_NAME = "vitals"

    COMMIT_SQL = (
        f"INSERT INTO {TABLE_NAME} (measured_on, weight_lb, bp_systolic, "
        "bp_diastolic, heart_bpm, notes) VALUES "
        "(?, ?, ?, ?, ?, ?)"
    )

    def to_sql_params(self) -> tuple:
        """
        Casts this object into a tuple in the order described above.
        (It will be ready to be inserted into a parameterized query.)
        """

        return (
            self.measured_on, self.weight_lb, self.bp_systolic,
            self.bp_diastolic, self.heart_bpm, self.notes
        )
