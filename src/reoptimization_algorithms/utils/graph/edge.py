"""
Edge class

"""

from reoptimization_algorithms.utils.graph.base_edge import BaseEdge


class Edge(BaseEdge):
    """
    Edge class represented as source, destination and weight attributes

    Default weight as :py:attr:`Edge.DEFAULT_EDGE_WEIGHT`

    :param source: Source vertex key
    :type source: str
    :param destination: Destination vertex key
    :type destination: str
    :param weight: Weight
    :type weight: float, optional (default = None)
    """

    def __init__(self, source: str, destination: str, weight: float = None):
        """
        Edge class represented as source, destination and weight attributes

        Default weight as :py:attr:`Edge.DEFAULT_EDGE_WEIGHT`

        :param source: Source vertex key
        :type source: str
        :param destination: Destination vertex key
        :type destination: str
        :param weight: Weight
        :type weight: float, optional (default = None)
        """
        self._source = source
        self._destination = destination
        if weight is None:
            weight = self.DEFAULT_EDGE_WEIGHT
        self._weight = weight

    @property
    def DEFAULT_EDGE_WEIGHT(self) -> float:
        """
        Default Edge Weight

        :return: 1
        """
        return 1

    @property
    def source(self) -> str:
        """
        Source vertex key

        :return: Vertex key
        """
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        """
        Source vertex key setter

        :param source: Source vertex key
        :type source: str

        :return: None
        """
        self._source = source

    @property
    def destination(self) -> str:
        """
        Destination vertex key

        :return: Destination vertex key
        """
        return self._destination

    @destination.setter
    def destination(self, destination: str) -> None:
        """
        Destination vertex key setter
        :param destination: Destination vertex key
        :type destination: str

        :return: None
        """
        self._destination = destination

    @property
    def weight(self) -> float:
        """
        Edge weight

        :return: Edge weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float) -> None:
        """
        Edge weight setter
        :param weight: Edge weight
        :type weight: float

        :return: None
        """
        self._weight = weight
