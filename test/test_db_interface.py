from runningtracker.db.db_interface import (
    commit, get_db, DATABASE_NAME, get_last_n_datapoints
)
from runningtracker.db.models.activity_datapoint import (
    ActivityDatapoint, get_last_n_cooper
)
from .mock.mock_models import MOCK_VITALS_DATAPOINT, MOCK_ACTIVITY_DATAPOINT
from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from unittest import TestCase
from os import unlink


class TestDbInterface(TestCase):
    def setUp(self) -> None:
        pass

    def test_can_commit_vitals_datapoint(self):
        commit(MOCK_VITALS_DATAPOINT)

        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM vitals")

        assert type(VitalsDatapoint(
            **cursor.fetchone()
        )) is VitalsDatapoint

    def test_can_commit_activity_datapoint(self):
        commit(MOCK_VITALS_DATAPOINT)
        commit(MOCK_ACTIVITY_DATAPOINT)

        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM activity")
        result = ActivityDatapoint(**cursor.fetchone())
        assert type(result) is ActivityDatapoint
        assert result == MOCK_ACTIVITY_DATAPOINT

    def test_get_last_n_datapoints(self):
        test_datapoints = [
            MOCK_VITALS_DATAPOINT
            for n in range(5)
        ]

        for datapoint in test_datapoints:
            commit(datapoint)

        result = get_last_n_datapoints(
            data_type=VitalsDatapoint,
            n=5
        )

        assert len(result) == 5
        assert all([type(item) is VitalsDatapoint for item in result])
        for item in result:
            assert type(item) is VitalsDatapoint
            MOCK_VITALS_DATAPOINT.entry_id = item.entry_id
            assert item == MOCK_VITALS_DATAPOINT

    def test_get_last_n_cooper(self):
        test_datapoints = [
            MOCK_VITALS_DATAPOINT
            for n in range(5)
        ]

        test_datapoints += [
            MOCK_ACTIVITY_DATAPOINT
            for n in range(5)
        ]

        for datapoint in test_datapoints:
            commit(datapoint)

        result = get_last_n_cooper(n=5)

        assert len(result) == 5
        assert all([type(item) is ActivityDatapoint for item in result])

    def tearDown(self) -> None:
        try:
            unlink(DATABASE_NAME)
        except:  # noqa
            pass
