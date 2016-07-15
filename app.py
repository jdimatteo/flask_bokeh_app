from bokeh.embed import components
from bokeh.plotting import figure
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    plot = figure()
    plot.circle([1,2], [3,4])

    bokeh_js, bokeh_div = components(plot)

    return render_template('index.html',
                           bokeh_js=bokeh_js,
                           bokeh_div=bokeh_div)
