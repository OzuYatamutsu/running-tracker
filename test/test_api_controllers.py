from .mock.mock_models import (
    MOCK_ACTIVITY_DATAPOINT, MOCK_ACTIVITY_DATAPOINT_CROSS_TRAIN,
    MOCK_VITALS_DATAPOINT
)
from runningtracker.api.controllers import (
    cooper_vo2max, get_weight_trend, get_bp_trend, get_run_pace_trend,
    get_vo2_trend
)
from runningtracker.db.models.activity_datapoint import (
    ActivityDatapoint
)

from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
from runningtracker.db.models import activity_datapoint
from runningtracker.db import db_interface
from unittest import TestCase


class TestApiControllers(TestCase):
    def setUp(self):
        self.test_good_cooper_datapoint = MOCK_ACTIVITY_DATAPOINT
        self.test_bad_cooper_datapoint = MOCK_ACTIVITY_DATAPOINT_CROSS_TRAIN
        self.test_vitals_datapoints = [
            VitalsDatapoint(
                entry_id=MOCK_VITALS_DATAPOINT.entry_id + 1 + n,
                measured_on=MOCK_VITALS_DATAPOINT.measured_on,
                weight_lb=MOCK_VITALS_DATAPOINT.weight_lb - n,
                bp_systolic=MOCK_VITALS_DATAPOINT.bp_systolic - n,
                bp_diastolic=MOCK_VITALS_DATAPOINT.bp_diastolic - n,
                heart_bpm=MOCK_VITALS_DATAPOINT.heart_bpm - n,
                notes=MOCK_VITALS_DATAPOINT.notes
            ) for n in range(5)
        ]
        self.test_activity_datapoints = [
            ActivityDatapoint(
                entry_id=MOCK_ACTIVITY_DATAPOINT.entry_id + 1 + n,
                linked_to_vitals_entry=MOCK_VITALS_DATAPOINT,
                activity_type=MOCK_ACTIVITY_DATAPOINT.activity_type,
                distance_mi=MOCK_ACTIVITY_DATAPOINT.distance_mi,
                duration_min=MOCK_ACTIVITY_DATAPOINT.duration_min,
                duration_sec=MOCK_ACTIVITY_DATAPOINT.duration_sec - n,
                feels_like_temp_f=MOCK_ACTIVITY_DATAPOINT.feels_like_temp_f,
                steps_per_min=MOCK_ACTIVITY_DATAPOINT.steps_per_min,
                notes=MOCK_ACTIVITY_DATAPOINT.notes
            ) for n in range(5)
        ]

        self._original_get_last_n_datapoints = \
            db_interface.get_last_n_datapoints
        self._original_get_last_n_cooper = \
            activity_datapoint.get_last_n_cooper

    def _mock_get_last_n_vitals_query(self, *args, **kwargs):
        return self.test_vitals_datapoints

    def _mock_get_last_n_activity_query(self, *args, **kwargs):
        return self.test_activity_datapoints

    def _mock_get_last_n_cooper_query(self, *args, **kwargs):
        return self.test_activity_datapoints

    def test_can_calculate_cooper_from_good_datapoint(self):
        assert cooper_vo2max(MOCK_ACTIVITY_DATAPOINT) >= 48.99
        assert cooper_vo2max(MOCK_ACTIVITY_DATAPOINT) <= 49.00

    def test_cannot_calculate_cooper_from_bad_datapoint(self):
        try:
            cooper_vo2max(MOCK_ACTIVITY_DATAPOINT)
            assert False
        except AssertionError:
            assert True

    def test_get_weight_trend(self):
        db_interface.get_last_n_datapoints = self._mock_get_last_n_vitals_query
        assert not not get_weight_trend(5)  # TODO

    def test_get_bp_trend(self):
        db_interface.get_last_n_datapoints = self._mock_get_last_n_vitals_query
        assert not not get_bp_trend(5)  # TODO

    def test_get_run_pace_trend(self):
        db_interface.get_last_n_datapoints = \
            self._mock_get_last_n_activity_query
        assert not not get_run_pace_trend(5)  # TODO

    def test_get_vo2_trend(self):
        db_interface.get_last_n_datapoints = \
            self._mock_get_last_n_activity_query
        assert not not get_vo2_trend(5)  # TODO

    def tearDown(self):
        db_interface.get_last_n_datapoints = \
            self._original_get_last_n_datapoints
        activity_datapoint.get_last_n_cooper = \
            self._original_get_last_n_cooper
