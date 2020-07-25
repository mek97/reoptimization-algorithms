"""
Path vertex cover utility class
"""

from itertools import combinations, permutations
from typing import Set, List, Tuple, Union, Iterable

from reoptimization_algorithms.utils.graph.undirected_graph import UndirectedGraph


class PVCUtils:
    """
    Utility class for Path vertex cover problem
    """

    @staticmethod
    def is_k_pvc(graph: 'UndirectedGraph', vertices: Set['str'], k: int) -> bool:
        """
        Checks if the given candidate vertices are k path cover for the graph

        :param graph: Undirected graph
        :type graph: UndirectedGraph
        :param vertices: Vertices to check if they form k path cover
        :type vertices: Set['str']
        :param k: length of paths which should be covered
        :type k: int

        :return: Boolean

        Example
        ~~~~~~~

        .. code-block:: python

           from reoptimization_algortihms import PVCUtils

           graph = (UndirectedGraph().add_edge("4", "5").add_edge("40", "50")
                    .add_vertex("6").add_edge("4", "8").add_vertex("99"))
           print(PVCUtils.is_k_pvc(graph, {"4"}, 3)) # True
        """
        is_k_pvc = True
        for k_path in list(combinations(graph.get_vertices(), k)):
            k_path_set = set(k_path)
            if len(k_path_set.intersection(vertices)) == 0 and PVCUtils.is_vertex_set_path(graph, k_path_set):
                is_k_pvc = False
                break
        return is_k_pvc

    @staticmethod
    def is_vertex_set_path(graph: 'UndirectedGraph', vertices: Iterable['str']) -> bool:
        """
        Checks if the vertices form a k path in graph

        :param graph: Undirected graph
        :type graph: UndirectedGraph
        :param vertices: Vertices to check if they form k path cover
        :type vertices: Set['str']

        :return: Boolean

        Example
        ~~~~~~~

        .. code-block:: python

           from reoptimization_algortihms import PVCUtils

           graph = (UndirectedGraph().add_edge("4", "5").add_edge("40", "50")
                    .add_vertex("6").add_edge("4", "8").add_vertex("99"))
           print(PVCUtils.is_vertex_set_path(graph, {"4", "5", "8"})) # True
        """
        is_k_path = False
        for path_perm in list(permutations(vertices)):
            if PVCUtils.is_path(graph, path_perm):
                is_k_path = True
                break
        return is_k_path

    @staticmethod
    def is_path(graph: 'UndirectedGraph', path: Union[List['str'], Tuple['str']]) -> bool:
        """
        Checks if the path exists in the graph

        :param graph: Undirected graph
        :type graph: UndirectedGraph
        :param path: Path as a list of vertices
        :type path: Union[List['str'], Tuple['str']]

        :return: Boolean

        Example
        ~~~~~~~

        .. code-block:: python

            from reoptimization_algortihms import PVCUtils

            graph = (UndirectedGraph().add_edge("4", "5").add_edge("40", "50")
                    .add_vertex("6").add_edge("4", "8").add_vertex("99"))
            print(PVCUtils.is_path(graph, ["4"])) # True
        """
        is_k_path = True
        for v in range(0, len(path) - 1):
            if not graph.is_edge_exists(path[v], path[v + 1]):
                is_k_path = False
                break
        return is_k_path
