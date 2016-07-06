from bokeh.client import push_session
from bokeh.document import Document
from bokeh.embed import autoload_server
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import TextInput 
from bokeh.plotting import figure, curdoc

from flask import Flask, render_template

app = Flask(__name__)

def update_title(attrname, old, new):
    print "-------------- update_title called with args", attrname, old, new
    plot.title.text = text.value

# global plot/text to simplify for now
plot = figure()
plot.circle([1,2], [3,4])
text = TextInput(title="title", value='plot title')
text.on_change('value', update_title)
update_title(None, None, None)

@app.route('/')
def index():
    document = Document()
    inputs = widgetbox(text)
    document.add_root(row(inputs, plot, width=800))

    session = push_session(document)
    script = autoload_server(None, session_id=session.id)

    return render_template('index.html', bokeh_script=script)
