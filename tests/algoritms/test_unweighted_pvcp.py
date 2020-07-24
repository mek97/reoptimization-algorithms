from unittest import TestCase

from reoptimization_algorithms import UnweightedPVCP
from reoptimization_algorithms import Edge
from reoptimization_algorithms import UndirectedGraph


class TestUnweightedPVCP(TestCase):
    def test_re_optimization(self):
        old_graph = (UndirectedGraph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
                     .add_edge("4", "8").add_vertex("99"))
        attached_graph = UndirectedGraph().add_edge("90", "95")
        attach_edges = [Edge("4", "90")]
        output = UnweightedPVCP.reoptimize_ptas(old_graph, attached_graph, attach_edges, {"8"}, 3)
        assert len(output) == 1
