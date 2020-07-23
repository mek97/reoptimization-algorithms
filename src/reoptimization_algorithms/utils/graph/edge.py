from reoptimization_algorithms.utils.graph.base_edge import BaseEdge


class Edge(BaseEdge):
    DEFAULT_EDGE_WEIGHT = 1

    def __init__(self, source: str, destination: str, weight=None):
        self._source = source
        self._destination = destination
        if weight is None:
            weight = self.DEFAULT_EDGE_WEIGHT
        self._weight = weight

    @property
    def source(self) -> str:
        """
        source getter
        :return:
        """
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        """
        source setter
        :param source:
        :return:
        """
        self._source = source

    @property
    def destination(self) -> str:
        """
        destination getter
        :return:
        """
        return self._destination

    @destination.setter
    def destination(self, destination: str) -> None:
        """
        destination setter
        :param destination:
        :return:
        """
        self._destination = destination

    @property
    def weight(self) -> int:
        """
        weight getter
        :return:
        """
        return self._weight

    @weight.setter
    def weight(self, weight: int) -> None:
        """
        weight setter
        :param weight:
        :return:
        """
        self._weight = weight
