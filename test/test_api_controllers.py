from .mock.mock_models import (
    MOCK_ACTIVITY_DATAPOINT, MOCK_ACTIVITY_DATAPOINT_CROSS_TRAIN
)
from runningtracker.db.models.activity_type import ActivityType
from runningtracker.api.controllers import cooper_vo2max
from unittest import TestCase


class TestApiControllers(TestCase):
    def setUp(self):
        self.test_good_cooper_datapoint = MOCK_ACTIVITY_DATAPOINT
        self.test_bad_cooper_datapoint = MOCK_ACTIVITY_DATAPOINT_CROSS_TRAIN

    def test_can_calculate_cooper_from_good_datapoint(self):
        assert cooper_vo2max(MOCK_ACTIVITY_DATAPOINT) >= 48.99
        assert cooper_vo2max(MOCK_ACTIVITY_DATAPOINT) <= 49.00

    def test_cannot_calculate_cooper_from_bad_datapoint(self):
        try:
            cooper_vo2max(MOCK_ACTIVITY_DATAPOINT)
            assert False
        except AssertionError:
            assert True
