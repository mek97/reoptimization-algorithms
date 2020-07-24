from reoptimization_algorithms import UndirectedGraph


class TestUndirectedGraph:
    def test_is_edge_exists(self):
        test_undirected_graph = (UndirectedGraph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
                                 .add_vertex("6").add_edge("4", "8").delete_edge("4", "5").add_vertex("99")
                                 .delete_vertex("6"))

        assert all([a == b for a, b in zip(test_undirected_graph.get_edges(),
                                           [{'_source': '4', '_destination': '8', '_weight': 1},
                                            {'_source': '40', '_destination': '50', '_weight': 1},
                                            {'_source': '50', '_destination': '40', '_weight': 1},
                                            {'_source': '8', '_destination': '4', '_weight': 1}])])

        print(test_undirected_graph.graph_pretty())

        assert all([a == b for a, b in zip(test_undirected_graph.get_vertices(), ['4', '5', '40', '50', '8', '99'])])
