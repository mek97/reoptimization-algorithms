from abc import ABCMeta

from reoptimizations_algorithms.utils.graph import BaseEdge


class BaseVertex(metaclass=ABCMeta):
    """
    Base Vertex abstract class
    """

    @property
    def key(self) -> str:
        raise NotImplementedError

    @property
    def weight(self):
        raise NotImplementedError

    @weight.setter
    def weight(self, weight: int) -> None:
        raise NotImplementedError

    @property
    def neighbours(self):
        raise NotImplementedError

    @neighbours.setter
    def neighbours(self, neighbours) -> None:
        raise NotImplementedError

    def add_neighbour(self, neighbour: str, weight) -> 'BaseVertex':
        raise NotImplementedError

    def get_neighbour(self, neighbour: str) -> 'BaseEdge':
        raise NotImplementedError

    def update_neighbour(self, neighbour: str, weight) -> 'BaseVertex':
        raise NotImplementedError

    def update(self, weight: int) -> 'BaseVertex':
        raise NotImplementedError

    def delete_neighbour(self, neighbour: str) -> 'BaseEdge':
        raise NotImplementedError

    def degree(self) -> int:
        raise NotImplementedError