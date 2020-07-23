from copy import deepcopy
from typing import Dict, List

from reoptimization_algorithms.utils.graph.graph import Graph
from reoptimization_algorithms.utils.graph.vertex import Vertex


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

    def update_edge(self, vertex_1: str, vertex_2: str, weight: int) -> 'UndirectedGraph':
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

    def delete_edge(self, vertex_1: str, vertex_2: str) -> 'UndirectedGraph':
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

    def add_edge(self, vertex_1: str, vertex_2: str, weight: int = None) -> 'UndirectedGraph':
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

    def get_edges(self) -> List[Dict]:
        """
        Gets edges in the graph
        :return:
        """
        edges = super().get_edges()

        return edges

    def display(self):
        vertices = self.get_vertices()
        v_li = []
        for vertex_key in vertices:
            vv = vars(deepcopy(self.get_vertex(vertex_key)))
            for key in vv:
                if isinstance(vv[key], dict):
                    for k in vv[key]:
                        vv[key][k] = vars(vv[key][k])
            v_li.append(vv)
        edges = self.get_edges()
        n_set = set()
        e_li = []
        for edge in edges:
            key = "::".join(sorted([edge["_source"], edge["_destination"]]))
            if key not in n_set:
                n_set.add(key)
                e_li.append(edge)

        return {"vertices": v_li, "edges": e_li}
