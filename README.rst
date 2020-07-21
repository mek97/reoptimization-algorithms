*************************
Reoptimization Algorithms
*************************

This package implements some well known Reoptimization algorithms

.. contents:: Table of Contents


Goal/Features
=============
Currently, considerable efforts must be put to find optimal solution for NP-Hard problems.
Reoptimisation deals with, If given an optimal solution to a problem instance I\ :sub:`O`,
can we find a good approximated solution to instance I\ :sub:`N`, where I\ :sub:`N` is I\ :sub:`O` with some 'local' modifications?
The goal in this repository is to expose some well known reoptimization algorithms.

Notable references
~~~~~~~~~~~~~~~~~~

Reoptimization algortithms

* `Complexity and Approximation in Reoptimization <https://www.researchgate.net/publication/48445129_Complexity_and_Approximation_in_Reoptimization>`_
* `Reoptimization of Path Vertex Cover Problem <https://link.springer.com/chapter/10.1007/978-3-030-26176-4_30#:~:text=The%20objective%20in%20k%2Dpath,cover%20problem%20admits%20a%20PTAS.>`_

Approximation algorithms

* `Approximation algorithms <https://www.ics.uci.edu/~vazirani/book.pdf>`_
* `Approximation algorithms Wikipedia <https://en.wikipedia.org/wiki/Approximation_algorithm>`_





Implementation
==============

Implementation basically consists of

#. Having a graph data structure utility
#. Implementing the respective graph algorithm methods

Graph Data structure
~~~~~~~~~~~~~~~~~~~~
- The graph data structures implementation is based on an adjacency list representation.
- The graph adjacency structure is implemented as a Python dictionary of dictionaries, the outer dictionary is keyed by vertices and mapped to neighboring vertex forming an edge.
- Vertices and Edges are provided with a weight property
- Supports CRUD operations on vertices and edges of graph
- Reference `Adjacency list`_, Further read `Introduction to Graph Theory By Douglas Brent West`_

.. _Adjacency list: https://en.wikipedia.org/wiki/Adjacency_list
.. _Introduction to Graph Theory By Douglas Brent West: http://free-journal.umm.ac.id/files/file/igtpref.ps


Algorirhms
~~~~~~~~~~
 `TBD`


Usage
=====

Requirements
~~~~~~~~~~~~

* Python versions: 3.7, 3.8

Installation Command
~~~~~~~~~~~~~~~~~~~~


* Option 1

  To Install the stable latest package from pypi host

    `TBD`

* Option 2

  To install directly from this repository execute

    ``python setup.py install``


Contribution
============

Want to add or improvise the repository? Check out the `Contributing <https://github.com/mek97/repotimization-algorithms/blob/release-v0/CONTRIBUTING.rst>`_ documentation :)

