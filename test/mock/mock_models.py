from runningtracker.db.models.activity_datapoint import ActivityDatapoint
from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from runningtracker.db.models.activity_type import ActivityType
from datetime import date


MOCK_VITALS_DATAPOINT = VitalsDatapoint(
    entry_id=1,
    measured_on=date.today(),
    weight_lb=130,
    bp_systolic=120,
    bp_diastolic=90,
    heart_bpm=90,
    notes='mock_entry'
)

MOCK_ACTIVITY_DATAPOINT = ActivityDatapoint(
    # TODO omit entry_id
    entry_id=1,
    linked_to_vitals_entry=MOCK_VITALS_DATAPOINT,
    activity_type=ActivityType.RUN,
    distance_mi=1.5,
    duration_min=10,
    duration_sec=37,
    feels_like_temp_f=93,
    steps_per_min=150,
    notes='mock_entry'
)

MOCK_ACTIVITY_DATAPOINT_CROSS_TRAIN = ActivityDatapoint(
    # TODO omit entry_id
    entry_id=2,
    linked_to_vitals_entry=MOCK_VITALS_DATAPOINT,
    activity_type=ActivityType.CROSS_TRAINING,
    distance_mi=1.5,
    duration_min=10,
    duration_sec=37,
    feels_like_temp_f=93,
    steps_per_min=150,
    notes='mock_entry'
)