from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from flask import Flask, jsonify, request, render_template
import numpy as np
from bokeh.models import Range1d

app = Flask('Ejemplo Bokeh')
@app.route('/',methods=['GET'])
def bokeh():
    data=request.args.to_dict()
    a=int(data['a'])
    b=int(data['b'])
    n=int(data['n'])
    x=np.linspace(0,10,n)
    y=a*np.sin(b*x)
    fig = figure(plot_width=1280, plot_height=600)
    fig.line(x,y)
    left, right, bottom, top = 0, 10, -10, 10
    fig.x_range=Range1d(left, right)
    fig.y_range=Range1d(bottom, top)
    # magia html del bokeh
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    script, div = components(fig)
    # este html esta en la carpeta /templates
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html.encode('utf8')
app.run(host='0.0.0.0',  port=5002)
