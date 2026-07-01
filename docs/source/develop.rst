Contributing
############

We are glad to welcome any contributor.

Report bugs or propose enhancements through  `github bug tracker`_

_`github bug tracker`: https://github.com/sabricot/django-elasticsearch-dsl/issues


If you want to contribute, the code is on github:
https://github.com/sabricot/django-elasticsearch-dsl

Testing
=======


This project is configured with ``pyproject.toml`` and its dependencies are
locked in ``uv.lock``. The test dependencies live in the ``test`` extra.

Using `uv <https://docs.astral.sh/uv/>`_, create the environment and run the
tests with::

    $ uv sync --extra test
    $ uv run python runtests.py

Alternatively, create and activate your own virtual environment and install the
package with its test extra using pip::

    $ source <path-to-venv>/bin/activate
    $ pip install -e '.[test]'
    $ python runtests.py


For integration testing with a running Elasticsearch server::

    $ uv run python runtests.py --elasticsearch [localhost:9200]
    # or, inside an activated virtual environment:
    $ python runtests.py --elasticsearch [localhost:9200]


To run the tests against all supported Python and Django versions, use tox
(provided by the ``dev`` extra)::

    $ uv run --extra dev tox
    # or, inside an activated virtual environment:
    $ pip install -e '.[dev]'
    $ tox

TODO
====
 
- Add support for --using (use another Elasticsearch cluster) in management commands.
- Add management commands for mapping level operations (like update_mapping....).
- Generate ObjectField/NestField properties from a Document class.
- More examples.
- Better ``ESTestCase`` and documentation for testing


