Contributions
#############

Contributions are welcome and are greatly appreciated! Every little bit helps,
and credit will always be given.

New Algorithms
--------------
Open feature request for an algorithm inclusion

Make sure to add a detailed doc in ``docs/`` with official references, preferably ``.rst`` for ``.tex``

Report Bugs
-----------

Report bugs through `GitHub Issues <https://github.com/mek97/reoptimization-algorithms/issues/>`__.

Please report relevant information and preferably code that exhibits the problem.

Fix Bugs
--------

Look through the GitHub issues for bugs. Anything is open to whoever wants to implement it.

Implement Features
------------------
Add GitHub issues labeled "kind:feature" for feature requests

Any unassigned feature request issue is open to whoever wants to implement it.

Improve Documentation
---------------------

Documentation improvements are always welcomed, whether as part of the official docs,
in docstrings, ``docs/*.rst`` or even on the web as blog posts or articles.

Submit Feedback
---------------

The best way to send feedback is to `open an issue on GitHub <https://github.com/mek97/reoptimization-algorithms/issues>`__.

If you are proposing a new feature:

-   Explain in detail how it would work.
-   Contributions are always welcome :)


Pull Request Guidelines
-----------------------

Before you submit a pull request (PR) from your forked repo, check that it meets
these guidelines:

-   Include docs in ``README.rst`` and ``docsrc/source/content.rst`` and docstrings.

    Test docs using ``sphinx-build -q -b html docsrc/source docsrc/build``

    The repo uses `Sphinx autosummary extenstion <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`__ for generating docs

-   Include tests, either as doctests, unit tests, or both, to your pull
    request.

    The repo uses `Github Actions <https://help.github.com/en/actions>`__ to
    run the tests and `codecov <https://codecov.io/gh/mek97/reoptimization-algorithms>`__ to track coverage. You can set up on your fork if needed. It will help you make sure you do not
    break the build with your PR.

-   Strictly adhering PEP8 coding style guide.

-   Format the code using `black <https://github.com/psf/black>`__

    Coding style rules are enforced programmatically by flake8 and black.

-   When merging PRs, wherever possible try to use **Squash and Merge** instead of **Rebase and Merge**.

-   If your pull request adds functionality, make sure to update the docs as part
    of the same PR. Doc string is often sufficient. Make sure to follow the
    Sphinx compatible standards.

-   Run tests locally and run tests via ``tox -e py37`` for python 3.7 env and similarly for 3.6 and 3.8.

-   Create a pull request and make sure it works for Python 3.6, 3.7 and 3.8.

-   Adhere to guidelines for commit messages described in this `article <http://chris.beams.io/posts/git-commit/>`__.
    This makes the lives of those who come after you a lot easier.

Git Branches
------------

``master`` branch is the stable branch, should always be synced with latest release branch. All new feature PRs should target ``master`` branch and release specific PRs ``release-v*`` branch.
