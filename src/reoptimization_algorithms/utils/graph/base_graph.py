"""
Base Graph abstract class
"""

from abc import ABCMeta, abstractmethod

from reoptimization_algorithms.utils.graph.vertex import Vertex
from reoptimization_algorithms.utils.graph.edge import Edge


class BaseGraph(metaclass=ABCMeta):
    """
    Base Graph abstract class
    """

    @abstractmethod
    def add_vertex(self, vertex: str, weight: int = None) -> 'BaseGraph':
        raise NotImplementedError

    @abstractmethod
    def get_vertex(self, vertex: str) -> Vertex:
        raise NotImplementedError

    @abstractmethod
    def delete_vertex(self, vertex: str) -> 'BaseGraph':
        raise NotImplementedError

    @abstractmethod
    def update_vertex(self, vertex: str, weight: int) -> 'BaseGraph':
        raise NotImplementedError

    @abstractmethod
    def get_edge(self, source: str, destination: str) -> 'Edge':
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, source: str, destination: str, weight: int = None) -> 'BaseGraph':
        raise NotImplementedError

    @abstractmethod
    def delete_edge(self, source: str, destination: str) -> 'BaseGraph':
        raise NotImplementedError

    @abstractmethod
    def update_edge(self, source: str, destination: str, weight: int) -> 'BaseGraph':
        raise NotImplementedError
