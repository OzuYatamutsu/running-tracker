from runningtracker.db.models.activity_type import ActivityType
from runningtracker.db.models.datapoint import Datapoint
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ActivityDatapoint(Datapoint):
    """
    Describes an instance of physical activity.
    """

    timestamp: datetime
    activity_type: ActivityType
    distance_mi: float
    duration_min: int
    duration_sec: int
    temp_f: float
    notes: str

    COMMIT_SQL = (
        "INSERT INTO activity (timestamp, activity_type, distance_mi, "
        "distance_min, distance_sec, temp_f, notes) VALUES "
        "(?, ?, ?, ?, ?, ?, ?)"
    )

    def to_sql_params(self) -> tuple:
        """
        Casts this object into a tuple in the order described above.
        (It will be ready to be inserted into a parameterized query.)
        """

        return (
            self.timestamp, self.activity_type, self.distance_mi,
            self.duration_min, self.duration_sec, self.temp_f,
            self.notes
        )
