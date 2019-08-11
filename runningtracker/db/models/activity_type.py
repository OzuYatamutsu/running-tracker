from enum import Enum


class ActivityType(Enum):
    WALK = 'walk'
    RUN = 'run'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()
