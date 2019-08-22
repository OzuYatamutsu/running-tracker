from runningtracker.db.models.activity_datapoint import (
    ActivityDatapoint  # , get_last_n_cooper
)
# from runningtracker.db.models.vitals_datapoint import VitalsDatapoint
# from runningtracker.db.db_interface import get_last_n_datapoints
from runningtracker.db.models.activity_type import ActivityType
from typing import Tuple


def cooper_vo2max(activity: ActivityDatapoint) -> float:
    """
    Given a 1.5 mile run activity, returns a vo2max value.
    """

    assert activity.distance_mi == 1.5, \
        f"Must use distance of 1.5 miles to calculate vo2max! {activity}"
    assert activity.activity_type in [ActivityType.RUN, ActivityType.COOPER], \
        f"Must use a run activity to calculate vo2max! {activity}"

    return (483 / activity.duration_in_min()) + 3.5


def get_weight_trend(n=5) -> float:
    """
    Returns the average change in weight across the most recent
    n measurements (defaults to 5).
    """

    # last_n_measurements = get_last_n_datapoints(VitalsDatapoint, n)
    pass  # TODO
    raise NotImplementedError


def get_bp_trend(n=5) -> Tuple[float, float]:
    """
    Returns the average change in blood press across the most recent
    n measurements (defaults to 5). The first value is systolic change,
    the second value is diastolic change.
    """

    # last_n_measurements = get_last_n_datapoints(VitalsDatapoint, n)
    pass  # TODO
    raise NotImplementedError


def get_run_pace_trend(n=5) -> float:
    """
    Returns the average change in running pace across the most recent
    n measurements (defaults to 5).
    """

    # last_n_measurements = get_last_n_datapoints(ActivityDatapoint, n)
    pass  # TODO
    raise NotImplementedError


def get_vo2_trend(n=5) -> float:
    """
    Returns the average change in running pace across the most recent
    n measurements (defaults to 5).
    """

    # last_n_measurements = get_last_n_cooper(n)
    pass  # TODO
    raise NotImplementedError
