from runningtracker.db.db_interface import (
    commit, _get_db, DATABASE_NAME, get_last_n_datapoints
)
from runningtracker.db.models.activity_datapoint import ActivityDatapoint
from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from runningtracker.db.models.vo2_datapoint import Vo2Datapoint
from runningtracker.db.models.activity_type import ActivityType
from unittest import TestCase
from datetime import datetime
from os import unlink


class TestDbInterface(TestCase):
    def setUp(self) -> None:
        pass

    def test_can_commit_vitals_datapoint(self):
        commit(VitalsDatapoint(
            timestamp=datetime.now(),
            weight_lb=0.0,
            bp_systolic=0.0,
            bp_diastolic=0.0,
            heart_bpm=0,
            notes=""
        ))

        cursor = _get_db().cursor()
        cursor.execute("SELECT * FROM vitals")

        assert type(VitalsDatapoint(
            **cursor.fetchone()
        )) is VitalsDatapoint

    def test_can_commit_activity_datapoint(self):
        commit(ActivityDatapoint(
            timestamp=datetime.now(),
            activity_type=ActivityType.WALK,
            distance_mi=0.0,
            duration_min=0,
            duration_sec=0,
            temp_f=0.0,
            notes=""
        ))

        cursor = _get_db().cursor()
        cursor.execute("SELECT * FROM activity")

        assert type(ActivityDatapoint(
            **cursor.fetchone()
        )) is ActivityDatapoint

    def test_can_commit_vo2_datapoint(self):
        commit(Vo2Datapoint(
            timestamp=datetime.now(),
            duration_min=0,
            duration_sec=0,
            notes=""
        ))

        cursor = _get_db().cursor()
        cursor.execute("SELECT * FROM vo2")

        assert type(Vo2Datapoint(
            **cursor.fetchone()
        )) is Vo2Datapoint

    def test_get_last_n_datapoints(self):
        test_datapoints = [
            VitalsDatapoint(
                timestamp=datetime.now(),
                weight_lb=0.0,
                bp_systolic=0.0,
                bp_diastolic=0.0,
                heart_bpm=0,
                notes=f"{n}"
            ) for n in range(5)
        ]

        for datapoint in test_datapoints:
            commit(datapoint)

        result = get_last_n_datapoints(
            datapoint_type=VitalsDatapoint,
            n=5
        )

        assert len(result) == 5
        assert all([type(item) is VitalsDatapoint for item in result])

    def tearDown(self) -> None:
        try:
            unlink(DATABASE_NAME)
        except:  # noqa
            pass
