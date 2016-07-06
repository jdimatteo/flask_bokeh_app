Flask app with bokeh push_session, autoload_server, and widgets
=====================================================

Trying to get push_session, autoload_server, and widgets to work. 

The update_title call back is not called when the text changes.

In one terminal, run bokeh server::

    $ bokeh serve --host localhost:5000 --host localhost:5006

In another window, run flask::

    $ export FLASK_APP=app.py
    $ flask run

Go to http://localhost:5000/
