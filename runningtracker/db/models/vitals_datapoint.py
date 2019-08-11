from datetime import datetime
from dataclasses import dataclass


@dataclass
class VitalsDatapoint:
    """
    Describes a measurement of vital statistics at
    a specific time.
    """

    timestamp: datetime
    weight_lb: float
    bp_systolic: float
    db_diastolic: float
    heart_bpm: int
    notes: str
