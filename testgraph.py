import plotly.plotly as py
import plotly.graph_objs as go
from crawler_4_jynthe import crawl, dpm

crawl()

length = len(dpm)
xs = []
for i in range(0, length):
    xs.append(i)

# Create a trace
trace = go.Scatter(
    x = xs,
    y = dpm
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-line')