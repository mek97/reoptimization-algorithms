"""
Edge class

"""

from reoptimization_algorithms.utils.graph.base_edge import BaseEdge


class Edge(BaseEdge):
    """
    Edge class represented as source, destination and weight attributes

    ``DEFAULT_EDGE_WEIGHT`` is set to 1

    :param source: Source vertex key
    :type source: str
    :param destination: Destination vertex key
    :type destination: str
    :param weight: Weight
    :type weight: int
    """

    DEFAULT_EDGE_WEIGHT = 1

    def __init__(self, source: str, destination: str, weight=None):
        """
        Edge class represented as source, destination and weight attributes

        If weight is None then assign DEFAULT_EDGE_WEIGHT

        :param source: Source vertex key
        :type source: str
        :param destination: Destination vertex key
        :type destination: str
        :param weight: Weight
        :type weight: int
        """
        self._source = source
        self._destination = destination
        if weight is None:
            weight = self.DEFAULT_EDGE_WEIGHT
        self._weight = weight

    @property
    def source(self) -> str:
        """
        Source vertex key
        """
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        """
        Source setter
        :param source: Source vertex key
        :type source: str

        :return:
        """
        self._source = source

    @property
    def destination(self) -> str:
        """
        Destination vertex key
        """
        return self._destination

    @destination.setter
    def destination(self, destination: str) -> None:
        """
        Destination setter
        :param destination: Destination vertex key
        :type destination: str

        :return:
        """
        self._destination = destination

    @property
    def weight(self) -> int:
        """
        Edge weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight: int) -> None:
        """
        Edge weight setter
        :param weight: Edge weight
        :type weight: int

        :return:
        """
        self._weight = weight
