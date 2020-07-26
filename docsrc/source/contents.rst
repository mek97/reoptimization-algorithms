############
Introduction
############
Currently, considerable efforts must be put to find optimal solution for **NP-Hard** [4]_ problems.
Reoptimisation deals with, If given an optimal solution to a problem instance :math:`I_O`,
can we find a good approximated solution to instance :math:`I_N`, where :math:`I_N` is :math:`I_O`` with some 'local' modifications?
The goal is to expose some well known reoptimization algorithms. Some references [1]_ [2]_ [3]_.

.. [1] Escoffier, B., Bonifaci, V., Ausiello, G.: Complexity and approximation in reoptimization (02 2011),
   <https://doi.org/10.1142/9781848162778_0004>

.. [2] Vazirani, V.V.: Approximation algorithms. Springer (2001)
   <https://www.ics.uci.edu/~vazirani/book.pdf>

.. [3] `Wikipedia: Approximation algorithms <https://en.wikipedia.org/wiki/Approximation_algorithm>`_

.. [4] `Wikipedia: NP-Hard <https://en.wikipedia.org/wiki/NP-hardness>`_

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

| A graph :math:`G` is a pair of sets :math:`(V, E)`, where :math:`V` is the set of vertices and :math:`E` is the set of edges formed by pairs of vertices in :math:`V`
| An unordered graph is a graph where :math:`E` is formed by unordered pairs of vertices
| We consider path as ordered set of vertices where adjacent vertices forms an edge and by path length we refer as number of vertices in it
| We say a set of vertices covers a path if at least one vertex from the set belongs to the set of the vertices in the path

- The graph data structure implementation here is based on an adjacency list representation.
- The adjacency structure is implemented as a Python dictionary of dictionaries, the outer dictionary is keyed by vertices and mapped to neighboring vertex forming an edge.
- Vertices and Edges are provided with a weight property
- Supports CRUD operations on vertices and edges of graph
- References [5]_ [6]_ [7]_

.. [5] Introduction to Graph Theory. Prentice Hall (1996)

.. [6] `Wikipedia: Graph Theory <https://en.wikipedia.org/wiki/Graph_theory>`_

.. [7] `Wikipedia: Adjacency list <https://en.wikipedia.org/wiki/Adjacency_list>`_


Graph utilities

    - :py:obj:`Graph <reoptimization_algorithms.utils.graph.graph.Graph>` - Graph utilities class
    - :py:obj:`Undirected Graph <reoptimization_algorithms.utils.graph.undirected_graph.UndirectedGraph>` - Undirected utilities class
    - :py:obj:`Vertex <reoptimization_algorithms.utils.graph.vertex.Vertex>` - Vertex utilities class
    - :py:obj:`Edge <reoptimization_algorithms.utils.graph.edge.Edge>` - Edge utilities class


Algorithms
==========

Reoptimization of k Path vertex cover problems (k-PCVP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The objective in k Path vertex cover problem is to compute a minimum subset :math:`S` of the vertices in a graph :math:`G` such that :math:`S` covers all the paths of length :math:`k` in the graph

**Note** k-PVCP will be referred as minimum k-PVCP throughout the package


PTAS for unweighted k-PVCP under constant size graph insertion [8]_
___________________________________________________________________

PTAS [9]_ algorithm when a constant size graph is inserted to the old graph. By constant graph we mean a graph having constant number of vertices.

.. [8] Kumar M., Kumar A., Pandu Rangan C. (2019) Reoptimization of Path Vertex Cover Problem.
   In: Du DZ., Duan Z., Tian C. (eds) Computing and Combinatorics. COCOON 2019.
   Lecture Notes in Computer Science, vol 11653. Springer, Cham
   <https://link.springer.com/chapter/10.1007/978-3-030-26176-4_30>

.. [9] `Wikipedia: PTAS <https://en.wikipedia.org/wiki/Polynomial-time_approximation_scheme>`_

:py:meth:`UnweightedPVCP.reoptimize_ptas <reoptimization_algorithms.algorithms.unwtd_pvcp.UnweightedPVCP.reoptimize_ptas>` - Method to perform the algorithm

k-PVCP utilities
________________

Some utilities for k path vertex cover

* :py:meth:`PVCUtils.is_k_pvc <reoptimization_algorithms.utils.graph.pvc.PVCUtils.is_k_pvc>` - Method to check if a vertex set is a valid k path vertex cover
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

Want to add or improvise the repository? Check out the `Contributing <https://github.com/mek97/reoptimization-algorithms/blob/master/CONTRIBUTING.rst>`_ documentation :)

##################
Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* `Github <https://github.com/mek97/reoptimization-algorithms>`_
