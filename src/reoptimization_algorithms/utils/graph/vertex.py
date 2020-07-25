"""
Vertex class
"""

from typing import Dict

from reoptimization_algorithms.utils.graph.edge import Edge


class Vertex:
    """
    Vertex class having key, weight and adjacency dictionary of neighbours

    Default weight as :py:attr:`Vertex.DEFAULT_VERTEX_WEIGHT`

    :param key: Key
    :type key: str
    :param weight: Weight of the vertex
    :type weight: int
    :param neighbours: Neighbours of the vertex
    :type neighbours: Dict[str, Edge]
    """

    def __init__(self, key: str, weight: int = None, neighbours: Dict[str, 'Edge'] = None):
        """
        Vertex class having key, weight and adjacency dictionary of neighbours

        Default weight as :py:attr:`Vertex.DEFAULT_VERTEX_WEIGHT`

        :param key: Key
        :type key: str
        :param weight: Weight of the vertex
        :type weight: int
        :param neighbours: Neighbours of the vertex
        :type neighbours: Dict[str, Edge]
        """
        self.__key = key
        if weight is None:
            weight = self.DEFAULT_VERTEX_WEIGHT
        self._weight = weight

        if neighbours is None:
            neighbours = {}
        self._neighbours = neighbours

    @property
    def DEFAULT_VERTEX_WEIGHT(self) -> int:
        """
        Default Vertex weight

        :return: 1
        """
        return 1

    @property
    def key(self) -> str:
        """
        Vertex key

        :return: Vertex key
        """
        return self.__key

    @property
    def weight(self) -> int:
        """
        Vertex weight

        :return: Vertex weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight: int) -> None:
        """
        Vertex weight setter

        :param weight: Vertex weight
        :type weight: int

        :return: None
        """
        self._weight = weight

    @property
    def neighbours(self) -> Dict[str, 'Edge']:
        """
        Neighbouring vertices

        :return: Dictionary of neighbouring vertices as keys and values as edges
        """
        return self._neighbours

    @neighbours.setter
    def neighbours(self, neighbours: Dict[str, 'Edge']) -> None:
        """
        Neighbouring vertices

        :param neighbours: Dictionary of neighbouring vertices as keys and values as edges
        :type neighbours: Dict[str, Edge]

        :return: None
        """
        self._neighbours = neighbours

    def is_neighbour_exists(self, neighbour: str) -> bool:
        """
        Checks if neighbour exists

        :param neighbour: Neighbour vertex key
        :type neighbour: str

        :return: Boolean
        """
        return neighbour in self._neighbours

    def add_neighbour(self, neighbour: str, weight: int = None) -> 'Vertex':
        """
        Adds a neighbour, default edge weight as :py:attr:`Edge.DEFAULT_EDGE_WEIGHT`

        :param neighbour: Neighbour vertex key
        :type neighbour: str
        :param weight: Edge weight
        :type weight: int

        :return: Self
        """
        if self.is_neighbour_exists(neighbour):
            raise Exception(f'Neighbour {neighbour} already exists for {self.__key}, delete it first')
        self.neighbours[neighbour] = Edge(self.key, neighbour, weight)
        return self

    def get_neighbour(self, neighbour: str) -> 'Edge':
        """
        Gets a neighbour

        :param neighbour: Neighbour vertex key
        :type neighbour: str

        :return: Edge representing the neighbour
        """
        if not self.is_neighbour_exists(neighbour):
            raise Exception(f'Neighbour {neighbour} does not exists for {self.__key}, create it first')
        return self.neighbours.get(neighbour)

    def update_neighbour(self, neighbour: str, weight: int = None) -> 'Vertex':
        """
        Updates a neighbour, default edge weight as :py:attr:`Edge.DEFAULT_EDGE_WEIGHT`

        :param neighbour: Neighbour vertex key
        :type neighbour: str
        :param weight: Edge weight to update
        :type weight: int

        :return: Self
        """
        self.neighbours[neighbour] = Edge(self.key, neighbour, weight)
        return self

    def update_weight(self, weight: int) -> 'Vertex':
        """
        Updates vertex weight

        :param weight: Vertex weight
        :type weight: int

        :return: Self
        """
        self._weight = weight
        return self

    def delete_neighbour(self, neighbour: str) -> Edge:
        """
        Deletes a neighbour

        :param neighbour: Neighbour vertex key
        :type neighbour: str

        :return: Deleted Edge
        """
        if not self.is_neighbour_exists(neighbour):
            raise Exception(f'Neighbour {neighbour} does not exists for {self.__key}, create it first')
        return self.neighbours.pop(neighbour)

    def degree(self) -> int:
        """
        Gets degree of the vertex

        :return: Degree of the vertex
        """
        return len(self.neighbours)
