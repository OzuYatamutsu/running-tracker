from datetime import datetime
from dataclasses import dataclass


@dataclass
class Vo2Datapoint:
    """
    Describes metadata relating to a Cooper test measurement,
    used to calculate an approximation of VO2max.
    """

    timestamp: datetime
    duration_min: int
    duration_sec: int
    notes: str
