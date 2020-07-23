from itertools import combinations, chain
from math import ceil
from typing import Set, List

from reoptimization_algorithms.utils.graph.edge import Edge
from reoptimization_algorithms.utils.graph.pvc import PVCUtils
from reoptimization_algorithms.utils.graph.undirected_graph import UndirectedGraph


class UnweightedPVCP:

    @staticmethod
    def reoptimize(old_graph: 'UndirectedGraph', attach_graph: 'UndirectedGraph', attach_edges: List['Edge'],
                   old_solution: Set[str], k: int, epsilon=0.25) -> Set[str]:
        """
        PTAS for unweighted k path vertex cover under constant graph addition
        :param attach_edges:
        :param attach_graph:
        :param old_graph:
        :param old_solution:
        :param k:
        :param epsilon:
        :return:
        """
        v_o = set(old_graph.get_vertices())
        new_graph = old_graph.graph_union(attach_graph, attach_edges)
        v_n = set(new_graph.get_vertices())
        v_a = v_n.difference(v_o)

        if len(v_n) < k:
            return set()

        m = ceil(len(v_a) / epsilon)
        sol_1 = v_n
        for c in set(chain.from_iterable(combinations(v_n, r) for r in range(0, m + 1))):
            candidate_vertices = set(c)
            if len(candidate_vertices) < len(sol_1) and PVCUtils.is_k_pvc(new_graph, candidate_vertices, k):
                sol_1 = candidate_vertices
        sol_2 = v_a.union(old_solution)
        result = sol_1 if len(sol_1) < len(sol_2) else sol_2
        return result
