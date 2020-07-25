"""
Graph class
"""

import copy
from abc import ABC
from typing import Dict, List, TypeVar

from reoptimization_algorithms.errors.Error import InputError
from reoptimization_algorithms.utils.graph.base_graph import BaseGraph
from reoptimization_algorithms.utils.graph.edge import Edge
from reoptimization_algorithms.utils.graph.vertex import Vertex

T = TypeVar('T', bound='Graph')


class Graph(BaseGraph, ABC):
    """
    Graph data structure class, represented as dictionary with vertices as key mapped to neighbouring vertices

    T is a type var, bounded to this class, will refer to child class if inherited

    :param graph: Graph definition, if None then empty graph is instantiated
    :type graph: Dict[str, Vertex]


    Example
    ~~~~~~~

    .. code-block:: python

       from reoptimization_algortihms import Graph

       graph = Graph()
       graph = graph.add_vertex("4", 14) # Adding vertex
       graph.get_vertex("4") # Getting vertex
       graph = graph.update_vertex("4", 15) # Update vertex weight
       graph = graph.delete_vertex("4") # Deleting vertex
       graph = graph.add_edge("4", "5", 11) # Adding Edge
       graph.get_edge("4", "5") # Getting Edge
       graph = graph.update_edge("4", "5", 10) # Update Edge weight
       graph = graph.delete_edge("4", "5") # Deleting Edge

       # Add, Update and Deletes can be chained as follows
       graph = (Graph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
                .add_vertex("6").add_edge("4", "8").delete_edge("4", "5").add_vertex("99")
                .delete_vertex("6"))
    """

    def __init__(self, graph: Dict[str, 'Vertex'] = None):
        """
        Graph data structure class, represented as dictionary with vertices as key mapped to neighbouring vertices

        :param graph: Graph definition, if None then empty graph is instantiated
        :type graph: Dict[str, Vertex]
        """
        if graph is None:
            graph = {}
        self._graph = graph

    @property
    def graph(self) -> Dict[str, 'Vertex']:
        """
        Graph represented as dictionary with vertices as key mapped to neighbouring vertices
        """
        return self._graph

    @graph.setter
    def graph(self, graph: Dict[str, 'Vertex']) -> None:
        """
        Graph setter

        :param graph: Graph as dictionary of vertices to set
        :type graph: Dict[str, Vertex]

        :return: None
        """
        self._graph = graph

    def is_vertex_exists(self, vertex: str) -> bool:
        """
        Checks if the vertex exists in the graph

        :param vertex: Vertex key
        :type vertex: str
        :return: Boolean
        """
        return vertex in self._graph

    def get_vertex(self, vertex: str) -> 'Vertex':
        """
        Gets the vertex

        :param vertex: Vertex key
        :type vertex: str

        :return: Vertex
        """
        if not self.is_vertex_exists(vertex):
            raise Exception(f'Vertex {vertex} does not exists, create it first')

        return self._graph.get(vertex)

    def add_vertex(self: T, vertex: str, weight: int = None) -> T:
        """
        Adds a vertex to the graph, default weight as :py:obj:`Vertex.DEFAULT_VERTEX_WEIGHT`

        :param vertex: Vertex key
        :type vertex: str
        :param weight: Vertex weight
        :type weight: int

        :return: Self
        """
        if self.is_vertex_exists(vertex):
            raise Exception(f'Vertex {vertex} already exists, delete it first')

        self._graph[vertex] = Vertex(vertex, weight)
        return self

    def delete_vertex(self: T, vertex: str) -> T:
        """
        Deletes a vertex

        :param vertex: Vertex key
        :type vertex: str

        :return: Self
        """
        for v in self.get_vertices():
            vertex_obj = self.get_vertex(v)
            vertex_obj.is_neighbour_exists(vertex) and vertex_obj.delete_neighbour(vertex)

        self._graph.pop(vertex)
        return self

    def update_vertex(self: T, vertex: str, weight: int) -> T:
        """
        Updates vertex weight

        :param vertex: Vertex key
        :type vertex: str
        :param weight: Vertex weight
        :type weight: int

        :return: Self
        """
        self.get_vertex(vertex).weight = weight
        return self

    def get_vertices(self) -> List[str]:
        """
        Gets the list of vertices in the graph

        :return: List of vertices keys
        """
        return list(self._graph.keys())

    def get_isolated_vertices(self) -> List['Vertex']:
        """
        Gets isolated vertices in the graph

        :return: List of vertices
        """
        vertices = []
        for vertex in self.get_vertices():
            if not bool(self.get_vertex(vertex).neighbours):
                vertices.append(self.get_vertex(vertex))
                self.delete_vertex(vertex)
        return vertices

    def delete_isolated_vertices(self: T) -> T:
        """
        Deletes isolated vertices in the graph

        :return: Self
        """
        for vertex in self.get_isolated_vertices():
            self.delete_vertex(vertex.key)
        return self

    def is_edge_exists(self, source: str, destination: str) -> bool:
        """
        Checks if the edge exists in the graph

        :param source: Edge source
        :type source: str
        :param destination: Edge destination
        :type destination: str

        :return: Boolean
        """
        return self.is_vertex_exists(source) and self.get_vertex(source).is_neighbour_exists(destination)

    def get_edge(self, source: str, destination: str) -> 'Edge':
        """
        Gets edge from the graph

        :param source: Edge source
        :type source: str
        :param destination: Edge destination
        :type destination: str

        :return: Edge
        """
        return self.get_vertex(source).get_neighbour(destination)

    def add_edge(self: T, source: str, destination: str, weight: int = None) -> T:
        """
        Adds edge in the graph, default weight as :py:obj:`Edge.DEFAULT_EDGE_WEIGHT`

        :param source: Edge source
        :type source: str
        :param destination: Edge destination
        :type destination: str
        :param weight: Weight
        :type weight: int

        :return: Self
        """
        if not self.is_vertex_exists(source):
            self.add_vertex(source)

        if not self.is_vertex_exists(destination):
            self.add_vertex(destination)

        if self.is_edge_exists(source, destination):
            raise Exception(f'Edge stc: {source} dest: {destination} already exists, delete it first')

        self.get_vertex(source).add_neighbour(destination, weight)
        return self

    def delete_edge(self: T, source: str, destination: str) -> T:
        """
        Deletes the edge in the graph

        :param source: Edge source
        :type source: str
        :param destination: Edge destination
        :type destination: str

        :return: Self
        """
        self.get_vertex(source).delete_neighbour(destination)
        return self

    def update_edge(self: T, source: str, destination: str, weight: int) -> T:
        """
        Checks if the edge exists in the graph

        :param source: Edge source
        :type source: str
        :param destination: Edge destination
        :type destination: str
        :param weight: Weight
        :type weight: int

        :return: Self
        """
        self.get_vertex(source).add_neighbour(destination, weight)
        return self

    def get_edges(self) -> List[Dict]:
        """
        Gets list of Edges

        :return: List of dictionary having Edge source, destination and weight as keys
        """
        edges = []
        for vertex in self.get_vertices():
            vertex_obj = self.get_vertex(vertex)
            for destination in vertex_obj.neighbours:
                edges.append(vars(vertex_obj.neighbours[destination]))

        return edges

    def copy(self: T) -> T:
        """
        Return a deep copy of the graph

        :return: Copied Graph
        """
        return copy.deepcopy(self)

    def graph_union(self: T, attach_graph: T, attach_edges: List['Edge']) -> T:
        """
        Attaches the caller graph with attach graph and attachment edges, make sure the vertices are disjoint

        :param attach_graph: Graph to attach
        :type attach_graph: T
        :param attach_edges: Edges to connect with attach_graph
        :type attach_edges: List[Edge]

        :raise InputError: If Vertices of calling graph and attach graph are not disjoint

        :return: Self
        """
        if not set(self.get_vertices()).isdisjoint(set(attach_graph.get_vertices())):
            raise InputError({
                "calling_graph_vertices": self.get_vertices(),
                "attach_graph_edges": attach_graph.get_vertices()
            },
                "Vertices of calling graph and attach graph must be disjoint")

        graph = Graph(copy.deepcopy({**self.graph, **attach_graph.graph}))
        for edge in attach_edges:
            graph.add_edge(edge.source, edge.destination, edge.weight)
        return graph
