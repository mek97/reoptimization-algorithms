"""
Unweighted Path vertex cover reoptimization algorithms class
"""

from itertools import combinations, chain
from math import ceil
from typing import Set, List

from reoptimization_algorithms.utils.graph.edge import Edge
from reoptimization_algorithms.utils.graph.pvc import PVCUtils
from reoptimization_algorithms.utils.graph.undirected_graph import UndirectedGraph


class UnweightedPVCP:
    """
    Class containing reoptimization algorithms of unweighted path vertex cover
    """

    @staticmethod
    def reoptimize_ptas(old_graph: 'UndirectedGraph', attach_graph: 'UndirectedGraph', attach_edges: List[Edge],
                        old_solution: Set[str], k: int, epsilon: float = 0.25) -> Set[str]:
        """
        :math:`(1+\\epsilon)` PTAS approximation for reoptimization of  unweighted k path vertex cover under constant size graph insertion

         For formalisms and algorithm details refer - `Reoptimization of Path Vertex Cover Problem <https://link.springer.com/chapter/10.1007/978-3-030-26176-4_30#:~:text=The%20objective%20in%20k%2Dpath,cover%20problem%20admits%20a%20PTAS.>`_

        :param old_graph: Old graph
        :type old_graph: List[Edge]
        :param attach_graph: Constant size graph which is to be inserted
        :type attach_graph: UndirectedGraph
        :param attach_edges: Edges connecting the old graph and attach graph
        :type attach_edges: List[Edge]
        :param old_solution: Vertices denoting k-PVCP Solution to old graph
        :type old_solution: Set[str]
        :param k: length of paths to cover
        :type k: int
        :param epsilon: epsilon in :math:`(1+\\epsilon)` PTAS  approximation
        :type epsilon: float

        :return: Set of vertices

        Example
        ~~~~~~~

        .. code-block:: python

            from reoptimization_algortihms import UnweightedPVCP

            old_graph = (UndirectedGraph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
                         .add_vertex("6").add_edge("4", "8").add_vertex("99")
                         .delete_vertex("6"))
            attached_graph = UndirectedGraph().add_edge("90", "95")
            attach_edges = [Edge("4", "90")]
            solution = UnweightedPVCP.reoptimize_ptas(old_graph, attached_graph, attach_edges, {"8"}, 3)
            print(solution) # {"4"}
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
