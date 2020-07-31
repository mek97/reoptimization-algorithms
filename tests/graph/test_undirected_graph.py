import reoptimization_algorithms as ra


class TestUndirectedGraph:
    def test_graph_1(self):
        test_undirected_graph = (ra.UndirectedGraph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
                                 .add_vertex("6").add_edge("4", "8").delete_edge("4", "5").add_vertex("99")
                                 .delete_vertex("6"))

        assert all([a == b for a, b in zip(test_undirected_graph.get_edges(),
                                           [{'_source': '4', '_destination': '8', '_weight': 1},
                                            {'_source': '40', '_destination': '50', '_weight': 1},
                                            {'_source': '50', '_destination': '40', '_weight': 1},
                                            {'_source': '8', '_destination': '4', '_weight': 1}])])

        print(test_undirected_graph.graph_pretty())

        assert all([a == b for a, b in zip(test_undirected_graph.get_vertices(), ['4', '5', '40', '50', '8', '99'])])

    def test_graph_2(self):
        graph = ra.UndirectedGraph()
        graph = graph.add_vertex("4", 14)  # Adding vertex
        graph.get_vertex("4")  # Getting vertex
        graph = graph.update_vertex("4", 15)  # Update vertex weight
        graph = graph.delete_vertex("4")  # Deleting vertex
        graph = graph.add_edge("4", "5", 11)  # Adding Edge
        graph.get_edge("4", "5")  # Getting Edge
        graph = graph.update_edge("4", "5", 10)  # Update Edge weight

        assert all([a == b for a, b in zip(graph.get_edges(),[{'_source': '4', '_destination': '5', '_weight': 10}])])
        assert all([a == b for a, b in zip(graph.get_vertices(), ['4', '5', '40', '50', '8', '99'])])
