from typing import Dict, List

from reoptimization_algorithms.utils.graph import Edge
from reoptimization_algorithms.utils.graph.Graph import Graph
from reoptimization_algorithms.utils.graph.Vertex import Vertex


class UndirectedGraph(Graph):

    def __init__(self, graph: Dict[str, 'Vertex'] = None):
        """
        Undirected Graph data structure
        :param graph:
        """
        super().__init__(graph)
        if graph is None:
            graph = {}
        self._graph = graph

    def is_edge_exists(self, vertex_1: str, vertex_2: str) -> bool:
        """
        Checks if edge exists
        :param vertex_1:
        :param vertex_2:
        :return:
        """
        return super().is_edge_exists(vertex_1, vertex_2) and super().is_edge_exists(vertex_2, vertex_1)

    def update_edge(self, vertex_1: str, vertex_2: str, weight: int) -> 'Graph':
        """
        Updates edge weight
        :param vertex_1:
        :param vertex_2:
        :param weight:
        :return:
        """
        if not self.is_edge_exists(vertex_1, vertex_2):
            raise Exception(f'Edge stc: {vertex_1} dest: {vertex_2} does not exists, create it first')

        super().update_edge(vertex_1, vertex_2, weight)
        super().update_edge(vertex_2, vertex_1, weight)

        return self

    def delete_edge(self, vertex_1: str, vertex_2: str) -> 'Graph':
        """
        Deletes an edge
        :param vertex_1:
        :param vertex_2:
        :return:
        """
        if not self.is_edge_exists(vertex_1, vertex_2):
            raise Exception(f'Edge stc: {vertex_1} dest: {vertex_2} does not exists, create it first')

        super().delete_edge(vertex_1, vertex_2)
        super().delete_edge(vertex_2, vertex_1)

        return self

    def add_edge(self, vertex_1: str, vertex_2: str, weight: int = None) -> 'Graph':
        """
        Adds an edge
        :param vertex_1:
        :param vertex_2:
        :param weight:
        :return:
        """
        if self.is_edge_exists(vertex_1, vertex_2):
            raise Exception(f'Symmetric Edge ({vertex_1}, {vertex_2}) already exists, delete it first')

        super().add_edge(vertex_1, vertex_2, weight)
        super().add_edge(vertex_2, vertex_1, weight)

        return self

    def get_edges(self) -> List['Edge']:
        """
        Gets edges in the graph
        :return:
        """
        edges = super().get_edges()

        return edges
