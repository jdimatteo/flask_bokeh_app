from bokeh.client import push_session
from bokeh.embed import autoload_server
from bokeh.plotting import figure, curdoc
from bokeh.document import Document
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    plot = figure()
    plot.circle([1,2], [3,4])
    document = Document()
    document.add_root(plot)

    session = push_session(document)
    script = autoload_server(None, session_id=session.id)

    return render_template('index.html', bokeh_script=script)
