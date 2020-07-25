"""
Undirected Graph class
"""

from copy import deepcopy
from typing import Dict, List, Union, Any

from reoptimization_algorithms.utils.graph.graph import Graph
from reoptimization_algorithms.utils.graph.vertex import Vertex


class UndirectedGraph(Graph):
    """
    Undirected Graph data structure class, inheriting Graph class, represented as dictionary with vertices
     as key mapped to neighbouring vertices in a symmetric manner

    :param graph: Undirected graph definition, if None then empty graph is instantiated
    :type graph: Dict[str, Vertex]

    Example
    ~~~~~~~

    .. code-block:: python

       from reoptimization_algortihms import UndirectedGraph

       graph = UndirectedGraph()
       graph = graph.add_vertex("4", 14) # Adding vertex
       graph.get_vertex("4") # Getting vertex
       graph = graph.update_vertex("4", 15) # Update vertex weight
       graph = graph.delete_vertex("4") # Deleting vertex
       graph = graph.add_edge("4", "5", 11) # Adding Edge
       graph.get_edge("4", "5") # Getting Edge
       graph = graph.update_edge("4", "5", 10) # Update Edge weight
       graph = graph.delete_edge("4", "5") # Deleting Edge

       # Add, Update and Deletes can be chained as follows
       graph = (UndirectedGraph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
       .add_vertex("6").add_edge("4", "8").delete_edge("4", "5").add_vertex("99")
       .delete_vertex("6"))

    """

    def __init__(self, graph: Dict[str, 'Vertex'] = None):
        """
        Undirected Graph data structure class, inheriting Graph class, represented as dictionary with vertices
         as key mapped to neighbouring vertices in a symmetric manner

        :param graph: Undirected graph definition, if None then empty graph is instantiated
        :type graph: Dict[str, Vertex]

        """
        super().__init__(graph)
        if graph is None:
            graph = {}
        self._graph = graph

    def is_edge_exists(self, vertex_1: str, vertex_2: str) -> bool:
        """
        Checks if edge exists in the graph

        :param vertex_1: vertex 1 of the edge
        :type vertex_1: str
        :param vertex_2: vertex 2 of the edge
        :type vertex_2: str

        :return: Boolean
        """
        return super().is_edge_exists(vertex_1, vertex_2) and super().is_edge_exists(vertex_2, vertex_1)

    def update_edge(self, vertex_1: str, vertex_2: str, weight: int) -> 'UndirectedGraph':
        """
        Updates edge weight in the graph

        :param vertex_1: vertex 1 of the edge
        :type vertex_1: str
        :param vertex_2: vertex 2 of the edge
        :type vertex_2: str
        :param weight: Weight to change with
        :type weight: int

        :return: Self
        """
        if not self.is_edge_exists(vertex_1, vertex_2):
            raise Exception(f'Edge stc: {vertex_1} dest: {vertex_2} does not exists, create it first')

        super().update_edge(vertex_1, vertex_2, weight)
        super().update_edge(vertex_2, vertex_1, weight)

        return self

    def delete_edge(self, vertex_1: str, vertex_2: str) -> 'UndirectedGraph':
        """
        Deletes an edge in the graph

        :param vertex_1: vertex 1 of the edge
        :type vertex_1: str
        :param vertex_2: vertex 2 of the edge
        :type vertex_2: str

        :return: Self
        """
        if not self.is_edge_exists(vertex_1, vertex_2):
            raise Exception(f'Edge stc: {vertex_1} dest: {vertex_2} does not exists, create it first')

        super().delete_edge(vertex_1, vertex_2)
        super().delete_edge(vertex_2, vertex_1)

        return self

    def add_edge(self, vertex_1: str, vertex_2: str, weight: int = None) -> 'UndirectedGraph':
        """
        Adds an edge in the graph

        :param vertex_1: vertex 1 of the edge
        :type vertex_1: str
        :param vertex_2: vertex 2 of the edge
        :type vertex_2: str
        :param weight: Weight of the edge
        :type weight: int

        :return: Self
        """
        if self.is_edge_exists(vertex_1, vertex_2):
            raise Exception(f'Symmetric Edge ({vertex_1}, {vertex_2}) already exists, delete it first')

        super().add_edge(vertex_1, vertex_2, weight)
        super().add_edge(vertex_2, vertex_1, weight)

        return self

    def get_edges(self) -> List[Dict]:
        """
        Gets edges from the graph

        :return: List of dictionary having Edge source, destination and weight as keys
        """
        edges = super().get_edges()
        edge_key_set = set()
        symmetric_edges = []
        for edge in edges:
            key = "::".join(sorted([edge["_source"], edge["_destination"]]))
            if key not in edge_key_set:
                edge_key_set.add(key)
                symmetric_edges.append(edge)

        return symmetric_edges

    def graph_pretty(self) -> Dict[str, Union[List[Dict[str, Any]], List[dict]]]:
        """
        Returns the graph in the pretty format

        :return: Vertices as list of {'_Vertex__key': '4', '_weight': 1, '_neighbours': ..} and edges as list of
         dictionary of source, _destination and _weight
        """
        vertices = self.get_vertices()
        formatted_vertices = []
        for vertex_key in vertices:
            formatted_vertex = vars(deepcopy(self.get_vertex(vertex_key)))
            for key in formatted_vertex:
                if isinstance(formatted_vertex[key], dict):
                    for k in formatted_vertex[key]:
                        formatted_vertex[key][k] = vars(formatted_vertex[key][k])
            formatted_vertices.append(formatted_vertex)

        edges = self.get_edges()

        return {"vertices": formatted_vertices, "edges": edges}
