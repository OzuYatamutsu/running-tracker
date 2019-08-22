from runningtracker.db.models.activity_datapoint import ActivityDatapoint
from runningtracker.db.models.activity_type import ActivityType


def cooper_vo2max(activity: ActivityDatapoint) -> float:
    """
    Given a 1.5 mile run activity, returns a vo2max value.
    """

    assert activity.distance_mi == 1.5, \
        f"Must use distance of 1.5 miles to calculate vo2max! {activity}"
    assert activity.activity_type in [ActivityType.RUN, ActivityType.COOPER], \
        f"Must use a run activity to calculate vo2max! {activity}"

    return (483 / activity.duration_in_min()) + 3.5
