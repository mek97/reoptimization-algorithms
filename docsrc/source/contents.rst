############
Introduction
############
Currently, considerable efforts must be put to find optimal solution for NP-Hard problems.
Reoptimisation deals with, If given an optimal solution to a problem instance I\ :sub:`O`,
can we find a good approximated solution to instance I\ :sub:`N`, where I\ :sub:`N` is I\ :sub:`O` with some 'local' modifications?
The goal is to expose some well known reoptimization algorithms.

Notable references
==================

Reoptimization algortithms

* `Complexity and Approximation in Reoptimization <https://www.researchgate.net/publication/48445129_Complexity_and_Approximation_in_Reoptimization>`_

Approximation algorithms

* `Approximation algorithms <https://www.ics.uci.edu/~vazirani/book.pdf>`_
* `Wikipedia <https://en.wikipedia.org/wiki/Approximation_algorithm>`_

#####
Setup
#####

Requirements
============

* Python versions: >=3.6, <=3.8

Installation
============


* Option 1

  To Install the stable latest package from pypi host

    ``pip install reoptimization-algorithms``

* Option 2

  To install directly from `source <https://github.com/mek97/reoptimization-algorithms>`_ execute the following in source root directory

    ``python setup.py install``

#####
Usage
#####

Implementation basically consists of

#. Having a graph data structure utility
#. Implementing the respective graph algorithm methods

Graph Data structure
====================

| A graph G is a pair of sets (V, E), where V is the set of vertices and E is the set of edges formed by pairs of vertices in V
| An unordered graph is a graph where E is formed by unordered pairs of vertices
| We consider path as ordered set of vertices where adjacent vertices forms an edge and by path length we refer number of vertices in it
| We say a set of vertices covers a path if at least once vertex belongs to the vertex set of path

- The graph data structures implementation is based on an adjacency list representation.
- The graph adjacency structure is implemented as a Python dictionary of dictionaries, the outer dictionary is keyed by vertices and mapped to neighboring vertex forming an edge.
- Vertices and Edges are provided with a weight property
- Supports CRUD operations on vertices and edges of graph
- Reference `Adjacency list`_, Further read `Introduction to Graph Theory By Douglas Brent West`_

.. _Adjacency list: https://en.wikipedia.org/wiki/Adjacency_list
.. _Introduction to Graph Theory By Douglas Brent West: http://free-journal.umm.ac.id/files/file/igtpref.ps

Graph utilities

    - :py:obj:`Graph <reoptimization_algorithms.utils.graph.graph.Graph>` - Graph utilities class
    - :py:obj:`Undirected Graph <reoptimization_algorithms.utils.undirected_graph.undirected_graph.UndirectedGraph>` - Undirected utilities class
    - :py:obj:`Vertex <reoptimization_algorithms.utils.graph.vertex.Vertex>` - Vertex utilities class
    - :py:obj:`Edge <reoptimization_algorithms.utils.graph.edge.Edge>` - Edge utilities class



Algorithms
==========

Reoptimization of k Path vertex cover problems (k-PCVP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The objective in k-path vertex cover problem is to compute a minimum subset S of the vertices in a graph G such that S covers all the k paths in the graph

PTAS for unweighted k-PVCP under constant size graph insertion
______________________________________________________________

| PTAS algorithm when a constant size graph is inserted to old graph. By constant graph we mean a graph having constant number of vertices.
| For algorithm details refer `Reoptimization of Path Vertex Cover Problem <https://link.springer.com/chapter/10.1007/978-3-030-26176-4_30#:~:text=The%20objective%20in%20k%2Dpath,cover%20problem%20admits%20a%20PTAS.>`_

:py:meth:`UnweightedPVCP.reoptimize_ptas <reoptimization_algorithms.algorithms.unwtd_pvcp.UnweightedPVCP.reoptimize_ptas>` - Method to perform the algorithm

k-PVCP utilities
________________

Some utilities for k path vertex cover

* :py:meth:`PVCUtils.is_k_pvc <reoptimization_algorithms.utils.graph.pvc.PVCUtils.is_k_pvc>` - Method to check if a vertex set is a valid k path cover
* :py:meth:`PVCUtils.is_vertex_set_path <reoptimization_algorithms.utils.graph.pvc.PVCUtils.is_vertex_set_path>` - Method to check if a vertex set forms a path in the graph
* :py:meth:`PVCUtils.is_path <reoptimization_algorithms.utils.graph.pvc.PVCUtils.is_path>` - Method to check if a path exists in the graph



#####################
Package documentation
#####################

.. autosummary::
   :toctree: _autosummary
    :hidden:
   :template: recursive-module-template.rst
   :recursive:

   reoptimization_algorithms

############
Contribution
############

Want to add or improvise the repository? Check out the `Contributing <https://github.com/mek97/repotimization-algorithms/blob/release-v0/CONTRIBUTING.rst>`_ documentation :)

##################
Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* `Github <https://github.com/mek97/reoptimization-algorithms>`_
