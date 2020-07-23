from itertools import combinations, permutations
from typing import Set, List, Tuple, Union, Iterable

from reoptimization_algorithms.utils.graph.undirected_graph import UndirectedGraph


class PVCUtils:
    @staticmethod
    def is_k_pvc(graph: 'UndirectedGraph', candidate: Set['str'], k: int) -> bool:
        """
        Checks if the given candidate vertices are k path cover for the graph
        :param graph:
        :param candidate:
        :param k:
        :return:
        """
        is_k_pvc = True
        for k_path in list(combinations(graph.get_vertices(), k)):
            k_path_set = set(k_path)
            if len(k_path_set.intersection(candidate)) == 0 and PVCUtils.is_path(graph, k_path_set):
                is_k_pvc = False
                break
        return is_k_pvc

    @staticmethod
    def is_path(graph: 'UndirectedGraph', vertices: Iterable['str']):
        """
        Checks if the vertices form a k path in graph
        :param graph:
        :param vertices:
        :return:
        """
        is_k_path = False
        for path_perm in list(permutations(vertices)):
            if PVCUtils.is_path_valid(graph, path_perm):
                is_k_path = True
                break
        return is_k_path

    @staticmethod
    def is_path_valid(graph: 'UndirectedGraph', path: Union[List['str'], Tuple['str']]):
        """
        Checks if the path exists in the graph
        :param graph:
        :param path:
        :return:
        """
        is_k_path = True
        for v in range(0, len(path) - 1):
            if not graph.is_edge_exists(path[v], path[v + 1]):
                is_k_path = False
                break
        return is_k_path
