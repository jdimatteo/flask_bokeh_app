Flask app with bokeh push_session and autoload_server
=====================================================

Demonstrate push_session and autoload_server usage.

In one terminal, run bokeh server::

    $ bokeh serve --host localhost:5000 --host localhost:5006

In another window, run flask::

    $ export FLASK_APP=app.py
    $ flask run

Go to http://localhost:5000/
