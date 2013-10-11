
from numpy import cumprod, linspace, random
import time

from bokeh.sampledata.stocks import AAPL, FB, GOOG, IBM, MSFT
from bokeh.plotting import *
from bokeh.objects import GridPlot

def correlation():
    output_file("correlation.html", title="correlation.py example")
    hold()

    num_points = 300

    now = time.time()
    dt = 24*3600 # days
    dates = linspace(now, now + num_points*dt, num_points)
    acme = cumprod(random.lognormal(0.0, 0.04, size=num_points))
    choam = cumprod(random.lognormal(0.0, 0.04, size=num_points))

    line(dates, acme, color='#1F78B4', tools="pan,zoom,resize", legend='ACME')
    line(dates, choam, color='#FB9A99', legend='CHOAM')

    curplot().title = "Stock Returns"
    xgrid()[0].grid_line_dash=""
    xgrid()[0].grid_line_alpha=0.3
    ygrid()[0].grid_line_dash=""
    ygrid()[0].grid_line_alpha=0.3
    p1 = curplot()
    figure()

    scatter(acme, choam, color='#A6CEE3', radius=3, tools="pan,zoom,resize", legend='close')

    curplot().title = "ACME / CHOAM Correlations"
    xgrid()[0].grid_line_dash=""
    xgrid()[0].grid_line_alpha=0.3
    ygrid()[0].grid_line_dash=""
    ygrid()[0].grid_line_alpha=0.3
    p2 = curplot()
    gridplot([[p1],[p2]], name="correlation")
    # g = GridPlot(children=[[p1],[p2]])
    # g._id = "correlation"
    # session = p1.session
    # session.add(g)
    # session.plotcontext.children.append(g)
    return curplot()

if __name__ == "__main__":
    correlation()
    # open a browser
    show()

