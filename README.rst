*************************
Reoptimization Algorithms
*************************

.. image:: https://img.shields.io/pypi/v/reoptimization-algorithms.svg
   :target: https://pypi.org/project/reoptimization-algorithms/
   :alt: Latest Version

.. image:: https://github.com/mek97/reoptimization-algorithms/workflows/Unit%20tests/badge.svg
   :target: https://github.com/mek97/reoptimization-algorithms/

.. image:: https://codecov.io/gh/mek97/reoptimization-algorithms/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/mek97/reoptimization-algorithms/

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT


Package implementing some well known Reoptimization algorithms

.. image:: https://mek97.github.io/reoptimization-algorithms/_images/header.png

`Perterson Graph <https://en.wikipedia.org/wiki/Generalized_Petersen_grapht>`_ (Made using `GeoGebra <https://www.geogebra.org/?lang=en>`_)


.. contents:: **Table of contents**

============
Introduction
============
Currently, considerable efforts must be put to find optimal solution for NP-Hard problems.
Reoptimisation deals with, If given an optimal solution to a problem instance I\ :sub:`O`,
can we find a good approximated solution to instance I\ :sub:`N`, where I\ :sub:`N` is I\ :sub:`O` with some 'local' modifications?
The goal in this repository is to expose some well known reoptimization algorithms.

=====
Setup
=====

Requirements
~~~~~~~~~~~~

* (**Recommended**) Python versions: >=3.6, <=3.8

Installation
~~~~~~~~~~~~


* Option 1

  To Install the stable latest package from pypi host

    ``pip install reoptimization-algorithms``

* Option 2

  To install directly from this repository execute the following in repository root directory

    ``python setup.py install``


=============
Documentation
=============

Toy example
~~~~~~~~~~~
.. code-block:: python

            import reoptimization_algorithms as ra

            old_graph = (ra.UndirectedGraph().add_vertex("4").add_edge("4", "5").add_edge("40", "50")
                         .add_vertex("6").add_edge("4", "8").add_vertex("99").delete_vertex("6"))
            attached_graph = ra.UndirectedGraph().add_edge("90", "95")
            attach_edges = [ra.Edge("4", "90")]
            old_solution = {"8"}

            solution = ra.UnweightedPVCP.reoptimize_ptas(old_graph, attached_graph, attach_edges,
                                                         old_solution, k = 3)
            print(solution) # {"4"}


For detailed documentation and usage refer `here <https://mek97.github.io/reoptimization-algorithms/index.html>`_



==============
Implementation
==============

Implementation basically consists of

#. Having a graph data structure utility
#. Implementing the graph algorithms

Algorithms
~~~~~~~~~~

Algorithms implemented

* PTAS for Reoptimization of unweighted k-path vertex cover under constant size graph insertion



============
Contribution
============

Want to add or improvise the repository? Check out the `Contributing <https://github.com/mek97/reoptimization-algorithms/blob/master/CONTRIBUTING.rst>`_ documentation :)
