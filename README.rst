Flask app to embed a bokeh server app
=====================================

In one terminal, run bokeh server::

    $ bokeh serve --host localhost:5000 --host localhost:5006 sliders.py

In another window, run flask::

    $ export FLASK_APP=app.py
    $ flask run

Go to http://localhost:5000/
