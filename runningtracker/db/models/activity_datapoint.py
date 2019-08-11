from runningtracker.db.models.activity_type import ActivityType
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ActivityDatapoint:
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
