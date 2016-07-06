from bokeh.client import push_session
from bokeh.embed import autoload_server
from bokeh.plotting import figure, curdoc

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # figure() function auto-adds the figure to curdoc()
    plot = figure()
    plot.circle([1,2], [3,4])

    session = push_session(curdoc())
    script = autoload_server(plot, session_id=session.id)
    return render_template('index.html', bokeh_script=script)
