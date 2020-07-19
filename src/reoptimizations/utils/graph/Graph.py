from abc import ABC
from typing import Dict, List

from reoptimizations.utils.graph import Edge
from reoptimizations.utils.graph.BaseGraph import BaseGraph
from reoptimizations.utils.graph.Vertex import Vertex


class Graph(BaseGraph, ABC):

    def __init__(self, graph: Dict[str, 'Vertex'] = None):
        """
        Graph data structure class, represented as dictionary with vertices as key mapped to neighbours vertices
        :param graph: Graph definition
        """
        if graph is None:
            graph = {}
        self._graph = graph

    @property
    def graph(self) -> Dict[str, 'Vertex']:
        """
        Graph getter
        :return:
        """
        return self._graph

    @graph.setter
    def graph(self, graph: Dict[str, 'Vertex']) -> None:
        """
        Graph setter
        :param graph:
        :return:
        """
        self._graph = graph

    def is_vertex_exists(self, vertex: str) -> bool:
        """
        Checks if the vertex exists in the graph
        :param vertex:
        :return:
        """
        return vertex in self._graph

    def get_vertex(self, vertex: str) -> 'Vertex':
        """
        Gets the vertex
        :param vertex:
        :return:
        """
        if not self.is_vertex_exists(vertex):
            raise Exception(f'Vertex {vertex} does not exists, create it first')

        return self._graph.get(vertex)

    def add_vertex(self, vertex: str, weight: int = None) -> 'Graph':
        """
        Adds a vertex to the graph, default weight as Vertex.DEFAULT_VERTEX_WEIGHT
        :param vertex:
        :param weight:
        :return:
        """
        if self.is_vertex_exists(vertex):
            raise Exception(f'Vertex {vertex} already exists, delete it first')

        self._graph[vertex] = Vertex(vertex, weight)
        return self

    def delete_vertex(self, vertex: str) -> 'Graph':
        """
        Deletes a vertex
        :param vertex:
        :return:
        """
        for v in self.get_vertices():
            vertex_obj = self.get_vertex(v)
            vertex_obj.is_neighbour_exists(vertex) and vertex_obj.delete_neighbour(vertex)

        self._graph.pop(vertex)
        return self

    def update_vertex(self, vertex: str, weight: int) -> 'Graph':
        """
        Updates vertex weight
        :param vertex:
        :param weight:
        :return:
        """
        self.get_vertex(vertex).weight = weight
        return self

    def get_vertices(self) -> List[str]:
        """
        Gets the list of vertices in the graph
        :return:
        """
        return list(self._graph.keys())

    def get_isolated_vertices(self) -> List['Vertex']:
        """
        Gets isolated vertices in the graph
        :return:
        """
        vertices = []
        for vertex in self.get_vertices():
            if not bool(self.get_vertex(vertex).neighbours):
                vertices.append(self.get_vertex(vertex))
                self.delete_vertex(vertex)
        return vertices

    def delete_isolated_vertices(self) -> 'Graph':
        """
        Deletes isolated vertices
        :return:
        """
        for vertex in self.get_isolated_vertices():
            self.delete_vertex(vertex.key)
        return self

    def is_edge_exists(self, source: str, destination: str) -> bool:
        """
        Checks if the edge exists in the graph
        :param source:
        :param destination:
        :return:
        """
        return self.is_vertex_exists(source) and self.get_vertex(source).is_neighbour_exists(destination)

    def get_edge(self, source: str, destination: str) -> 'Edge':
        """
        Gets edge weight
        :param source:
        :param destination:
        :return:
        """
        return self.get_vertex(source).get_neighbour(destination)

    def add_edge(self, source: str, destination: str, weight: int = None) -> 'Graph':
        """
        Adds an edge in the graph, default weight as Edge.DEFAULT_EDGE_WEIGHT
        :param source:
        :param destination:
        :param weight:
        :return:
        """
        if not self.is_vertex_exists(source):
            self.add_vertex(source)

        if not self.is_vertex_exists(destination):
            self.add_vertex(destination)

        if self.is_edge_exists(source, destination):
            raise Exception(f'Edge stc: {source} dest: {destination} already exists, delete it first')

        self.get_vertex(source).add_neighbour(destination, weight)
        return self

    def delete_edge(self, source: str, destination: str) -> 'Graph':
        """
        Deletes edge from the graph
        :param source:
        :param destination:
        :return:
        """
        self.get_vertex(source).delete_neighbour(destination)
        return self

    def update_edge(self, source: str, destination: str, weight: int) -> 'Graph':
        """
        Updates edge weight
        :param source:
        :param destination:
        :param weight:
        :return:
        """
        self.get_vertex(source).add_neighbour(destination, weight)
        return self

    def get_edges(self) -> List['Edge']:
        """
        Gets list of Edges
        :return:
        """
        edges = []
        for vertex in self.get_vertices():
            vertex_obj = self.get_vertex(vertex)
            for destination in vertex_obj.neighbours:
                edges.append(vars(vertex_obj.neighbours[destination]))

        return edges
