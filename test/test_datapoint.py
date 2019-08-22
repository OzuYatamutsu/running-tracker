from .mock.mock_models import MOCK_ACTIVITY_DATAPOINT, MOCK_VITALS_DATAPOINT
from runningtracker.db.db_interface import _init_db
from unittest import TestCase
from sqlite3 import connect


class TestDatapoint(TestCase):
    def setUp(self) -> None:
        self.db = connect(":memory:")
        _init_db(self.db)

    def commit(self, datapoint):
        self.db.execute(
            datapoint.COMMIT_SQL, datapoint.to_sql_params()
        )

    def test_vitals_datapoint_has_valid_sql(self):
        self.commit(MOCK_VITALS_DATAPOINT)
        assert True

    def test_activity_datapoint_has_valid_sql(self):
        self.commit(MOCK_ACTIVITY_DATAPOINT)
        assert True
