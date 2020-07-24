from unittest import TestCase

from reoptimization_algorithms import PVCUtils
from reoptimization_algorithms import UndirectedGraph


class TestPVCUtils(TestCase):
    def test_is_k_pvc(self):
        graph = (UndirectedGraph().add_edge("4", "5").add_edge("40", "50")
                 .add_vertex("6").add_edge("4", "8").add_vertex("99"))
        assert PVCUtils.is_k_pvc(graph, {"4"}, 3)

    def test_is_vertex_set_path(self):
        graph = (UndirectedGraph().add_edge("4", "5").add_edge("40", "50")
                 .add_vertex("6").add_edge("4", "8").add_vertex("99"))
        assert PVCUtils.is_vertex_set_path(graph, {"4", "5", "8"})

    def test_is_path(self):
        graph = (UndirectedGraph().add_edge("4", "5").add_edge("40", "50")
                 .add_vertex("6").add_edge("4", "8").add_vertex("99"))
        assert PVCUtils.is_path(graph, ["4"])
