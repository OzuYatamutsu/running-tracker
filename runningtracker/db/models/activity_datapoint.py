from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from runningtracker.db.db_interface import get_vitals_datapoint_by_id
from runningtracker.db.models.activity_type import ActivityType
from runningtracker.db.models.datapoint import Datapoint
from dataclasses import dataclass
from typing import Optional


@dataclass
class ActivityDatapoint(Datapoint):
    """
    Describes an instance of physical activity.
    """

    # (Entry ID is only used for db-Python deserialization.)
    entry_id: Optional[int]
    linked_to_vitals_entry: VitalsDatapoint
    activity_type: ActivityType
    distance_mi: float
    duration_min: int
    duration_sec: int
    feels_like_temp_f: float
    steps_per_min: float
    notes: str

    TABLE_NAME = "activity"

    COMMIT_SQL = (
        f"INSERT INTO {TABLE_NAME} (linked_to_vitals_entry, activity_type, "
        f"distance_mi, duration_min, duration_sec, feels_like_temp_f, "
        f"steps_per_min, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    )

    def __post_init__(self):
        # Cast the activity type to an ActivityType enum if needed
        if type(self.activity_type) is not ActivityType:
            self.activity_type = ActivityType(self.activity_type)

        # Resolve the vitals entry ID into an object if needed
        if type(self.linked_to_vitals_entry) is VitalsDatapoint:
            return

        self.linked_to_vitals_entry = get_vitals_datapoint_by_id(
            entry_id=self.linked_to_vitals_entry
        )

    def to_sql_params(self) -> tuple:
        """
        Casts this object into a tuple in the order described above.
        (It will be ready to be inserted into a parameterized query.)
        """

        assert self.linked_to_vitals_entry.entry_id is not None,\
            f"Cannot serialize params against uncommitted vitals object!"

        return (
            self.linked_to_vitals_entry.entry_id, str(self.activity_type),
            self.distance_mi, self.duration_min, self.duration_sec,
            self.feels_like_temp_f, self.steps_per_min, self.notes
        )

    def duration_in_min(self) -> float:
        """
        Casts the minutes and seconds duration into a
        total duration in minutes.
        """

        return self.duration_min + (self.duration_sec / 60)

    def duration_in_sec(self) -> int:
        """
        Casts the minutes and seconds duration into a
        total duration in seconds.
        """

        return (60 * self.duration_min) + self.duration_sec
