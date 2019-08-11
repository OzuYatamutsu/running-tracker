from enum import Enum


class ActivityType(Enum):
    """
    Describes the type of activity to track data against.
    """

    WALK = 'walk'
    RUN = 'run'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()
