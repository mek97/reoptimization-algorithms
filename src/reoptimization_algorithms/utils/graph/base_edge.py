"""
Base Edge abstract class
"""

from abc import ABCMeta


class BaseEdge(metaclass=ABCMeta):
    """
    Base Edge abstract class
    """

    @property
    def source(self) -> str:
        raise NotImplementedError

    @source.setter
    def source(self, source: str) -> None:
        raise NotImplementedError

    @property
    def destination(self) -> str:
        raise NotImplementedError

    @destination.setter
    def destination(self, destination: str) -> None:
        raise NotImplementedError

    @property
    def weight(self):
        raise NotImplementedError

    @weight.setter
    def weight(self, weight: int) -> None:
        raise NotImplementedError
