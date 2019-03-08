GSoc 2019 submission 
====================

This is my submission for the Ganga memory optimization project for GSoC 2019.
 

Task 1
------

1. Clone this repository. The ``task1a-hello-world.png`` shows the hello world job being run. Instructions follow for task 1b.

2. Change directory to folder called ``task-1``.

3. Run the ``ganga-job.py`` file as:

.. code-block:: bash

    ganga -i ganga-job.py

4. Navigate to the directory suggested by ``job.outputdir`` to check output.

Note 1 : This requires that the pages of CERN.pdf already be split using the provided ``split-pdf.py``, as follows (however, the split pages are already provided):

.. code-block:: bash

    python split-pdf.py CERN.pdf

Note 2 : Ensure that at the Ganga prompt, you use ``chmod`` to set executable permissions for ``count-word.sh`` and ``custommerge.py``:

.. code-block:: bash

   $ !chmod -x FILENAME

Explanation for task 1
----------------------

The main script ``ganga-job.py`` calls ``count-word.sh`` for counting words, and then a custom merger written at ``custommerge.py`` for merging output (by summation) to the output folder.