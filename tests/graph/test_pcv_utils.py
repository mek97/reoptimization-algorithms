from unittest import TestCase

import reoptimization_algorithms as ra


class TestPVCUtils(TestCase):
    def test_is_k_pvc(self):
        graph = (
            ra.UndirectedGraph()
            .add_edge("4", "5")
            .add_edge("40", "50")
            .add_vertex("6")
            .add_edge("4", "8")
            .add_vertex("99")
        )
        assert ra.PVCUtils.is_k_pvc(graph, {"4"}, 3)

    def test_is_vertex_set_path(self):
        graph = (
            ra.UndirectedGraph()
            .add_edge("4", "5")
            .add_edge("40", "50")
            .add_vertex("6")
            .add_edge("4", "8")
            .add_vertex("99")
        )
        assert ra.PVCUtils.is_vertex_set_path(graph, {"4", "5", "8"})

    def test_is_path(self):
        graph = (
            ra.UndirectedGraph()
            .add_edge("4", "5")
            .add_edge("40", "50")
            .add_vertex("6")
            .add_edge("4", "8")
            .add_vertex("99")
        )
        assert ra.PVCUtils.is_path(graph, ["4"])
