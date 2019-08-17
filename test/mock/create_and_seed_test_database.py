from .mock_models import MOCK_ACTIVITY_DATAPOINT, MOCK_VITALS_DATAPOINT
from runningtracker.db.db_interface import commit, SCHEMA_LOCATION
from pathlib import Path
from datetime import date, timedelta
from random import randint
MOCK_DATAPOINT_COUNT = 100


def main():
    for i in range(MOCK_DATAPOINT_COUNT):
        vitals_datapoint = MOCK_VITALS_DATAPOINT
        vitals_datapoint.measured_on = (
            date.today() - timedelta(days=MOCK_DATAPOINT_COUNT - i)
        )
        activity_datapoint = MOCK_ACTIVITY_DATAPOINT

        # Randomize mock data for vitals
        vitals_datapoint.weight_lb = randint(120, 130)
        vitals_datapoint.bp_systolic = randint(110, 130)
        vitals_datapoint.bp_diastolic = randint(60, 90)
        vitals_datapoint.heart_bpm = randint(80, 90)

        # Randomize mock data for activity
        activity_datapoint.linked_to_vitals_entry = vitals_datapoint
        activity_datapoint.distance_mi = float(randint(3, 10))
        activity_datapoint.duration_min = randint(30, 60)
        activity_datapoint.duration_sec = randint(0, 60)
        activity_datapoint.feels_like_temp_f = randint(65, 90)
        activity_datapoint.steps_per_min = randint(80, 150)

        # Commit both
        print(f"Committing mock data: {vitals_datapoint}")
        commit(vitals_datapoint)
        print(f"Committing mock data: {activity_datapoint}")
        commit(activity_datapoint)

if __name__ == '__main__':
    main()
