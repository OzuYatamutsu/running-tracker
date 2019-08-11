from abc import ABCMeta, abstractmethod


class Datapoint(metaclass=ABCMeta):
    """
    Describes a series of values at a given time.
    """

    @property
    @abstractmethod
    def COMMIT_SQL(self):
        """
        What SQL statement should we run to commit this
        object to the database?
        """

        raise NotImplementedError

    @abstractmethod
    def to_sql_params(self) -> tuple:
        """
        Casts this object into a tuple in the order described above.
        (It will be ready to be inserted into a parameterized query.)
        """

        raise NotImplementedError
