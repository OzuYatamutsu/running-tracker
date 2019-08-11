from runningtracker.db.models.activity_datapoint import ActivityDatapoint
from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from runningtracker.db.models.vo2_datapoint import Vo2Datapoint
from runningtracker.db.models.activity_type import ActivityType
from runningtracker.db.models.datapoint import Datapoint
from runningtracker.db.db_interface import _init_db
from dataclasses import dataclass
from unittest import TestCase
from datetime import datetime
from sqlite3 import connect


class TestDatapoint(TestCase):
    def setUp(self) -> None:
        self.db = connect(":memory:")
        _init_db(self.db)

    def commit(self, datapoint):
        self.db.execute(
            datapoint.COMMIT_SQL, datapoint.to_sql_params()
        )

    def test_incomplete_datapoint_subclassing_throws_error(self):
        @dataclass
        class BadDatapoint(Datapoint):
            """
            This should fail. It does not implement
            required fields/methods
            """
            value: int

        try:
            bad_datapoint = BadDatapoint(value=1)  # noqa
            assert bad_datapoint.value == 1
            assert False
        except TypeError:
            assert True

    def test_vitals_datapoint_has_valid_sql(self):
        datapoint = VitalsDatapoint(
            timestamp=datetime.now(),
            weight_lb=0.0,
            bp_systolic=0.0,
            bp_diastolic=0.0,
            heart_bpm=0,
            notes=""
        )

        self.commit(datapoint)
        assert True

    def test_activity_datapoint_has_valid_sql(self):
        datapoint = ActivityDatapoint(
            timestamp=datetime.now(),
            activity_type=ActivityType.WALK,
            distance_mi=0.0,
            duration_min=0,
            duration_sec=0,
            temp_f=0.0,
            notes=""
        )

        self.commit(datapoint)
        assert True

    def test_vo2_datapoint_has_valid_sql(self):
        datapoint = Vo2Datapoint(
            timestamp=datetime.now(),
            duration_min=0,
            duration_sec=0,
            notes=""
        )

        self.commit(datapoint)
        assert True
