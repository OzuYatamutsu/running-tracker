from datetime import datetime
from dataclasses import dataclass


@dataclass
class VitalsDatapoint:
    timestamp: datetime
    weight_lb: float
    bp_systolic: float
    db_diastolic: float
    heart_bpm: int
    notes: str
