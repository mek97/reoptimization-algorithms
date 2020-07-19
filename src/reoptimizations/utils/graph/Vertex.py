from typing import Dict

from reoptimizations.utils.graph.Edge import Edge


class Vertex:
    DEFAULT_VERTEX_WEIGHT = 1

    def __init__(self, key: str, weight: int = None, neighbours: Dict[str, 'Edge'] = None):
        """
        Vertex class
        :param key: Key associated to the graph
        :param weight: Weight of the vertex
        :param neighbours: Neighbours of the vertex
        """
        self.__key = key
        if weight is None:
            weight = self.DEFAULT_VERTEX_WEIGHT
        self._weight = weight

        if neighbours is None:
            neighbours = {}
        self._neighbours = neighbours

    @property
    def key(self) -> str:
        """
        key getter
        :return:
        """
        return self.__key

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

    @property
    def neighbours(self) -> Dict[str, 'Edge']:
        """
        neighbours getter
        :return:
        """
        return self._neighbours

    @neighbours.setter
    def neighbours(self, neighbours: Dict[str, 'Edge']) -> None:
        """
        neighbours setter
        :param neighbours:
        :return:
        """
        self._neighbours = neighbours

    def is_neighbour_exists(self, neighbour: str) -> bool:
        """
        Checks if neighbour exists
        :param neighbour:
        :return:
        """
        return neighbour in self._neighbours

    def add_neighbour(self, neighbour: str, weight: int = None) -> 'Vertex':
        """
        Adds a neighbour, default edge weight as DEFAULT_EDGE_WEIGHT
        :param neighbour:
        :param weight:
        :return:
        """
        if self.is_neighbour_exists(neighbour):
            raise Exception(f'Neighbour {neighbour} already exists for {self.__key}, delete it first')
        self.neighbours[neighbour] = Edge(self.key, neighbour, weight)
        return self

    def get_neighbour(self, neighbour: str) -> 'Edge':
        """
        Gets a neighbour
        :param neighbour:
        :return:
        """
        if not self.is_neighbour_exists(neighbour):
            raise Exception(f'Neighbour {neighbour} does not exists for {self.__key}, create it first')
        return self.neighbours.get(neighbour)

    def update_neighbour(self, neighbour: str, weight: int = None) -> 'Vertex':
        """
        Updates a neighbour
        :param neighbour:
        :param weight:
        :return:
        """
        self.neighbours[neighbour] = Edge(self.key, neighbour, weight)
        return self

    def update_weight(self, weight: int) -> 'Vertex':
        """
        Updates weight
        :param weight:
        :return:
        """
        self._weight = weight
        return self

    def delete_neighbour(self, neighbour: str) -> Edge:
        """
        Deletes a neighbour
        :param neighbour:
        :return:
        """
        if not self.is_neighbour_exists(neighbour):
            raise Exception(f'Neighbour {neighbour} does not exists for {self.__key}, create it first')
        return self.neighbours.pop(neighbour)

    def degree(self) -> int:
        """
        Gets degree of the vertex
        :return:
        """
        return len(self.neighbours)
