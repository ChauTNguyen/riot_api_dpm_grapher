import plotly.plotly as py
import plotly.graph_objs as go
from crawler_4_jynthe import crawl, avg_dpms

# snownobo
dpm_snownobo = crawl(49188821)

length = len(dpm_snownobo)
xs_snownobo = []
for i in range(0, length):
    xs_snownobo.append(i)
trace_snownobo = go.Scatter(
    x = xs_snownobo,
    y = dpm_snownobo,
    mode = "line + markers",
    name = "Snownobo",
    line = dict(
        color=('rgb(0, 255, 0)'),
        width=2
    )
)

print()

# sky_fear
dpm_sky_fear = crawl(62372968)
xs_sky_fear = []
for i in range(0, length): # same length as jynthe's
    xs_sky_fear.append(i)
trace_sky_fear = go.Scatter(
    x = xs_sky_fear,
    y = dpm_sky_fear,
    mode = "line + markers",
    name = "SKY Fear",
    line = dict(
        color=('rgb(0, 0, 255)'),
        width=2)
)

# liquid_fabbbyyy
dpm_liquid_fabbbyyy = crawl(34287847)
xs_liquid_fabbbyyy = []
for i in range(0, length): # same length as jynthe's
    xs_liquid_fabbbyyy.append(i)
trace_liquid_fabbbyyy = go.Scatter(
    x = xs_liquid_fabbbyyy,
    y = dpm_liquid_fabbbyyy,
    mode = "line + markers",
    name = "Liquid_Fabbbyyy",
    line = dict(
        color=('rgb(255, 0, 0)'),
        width=2)
)

# doublelift
dpm_doublelift = crawl(20132258)
xs_doublelift = []
for i in range(0, length):
    xs_doublelift.append(i)
trace_doublelift = go.Scatter(
    x = xs_doublelift,
    y = dpm_doublelift,
    mode = "line + markers",
    name = "Doublelift",
    line = dict(
        color=('rgb(0, 0, 0'),
        width=2
    )
)

data = [trace_snownobo, trace_sky_fear, trace_liquid_fabbbyyy, trace_doublelift]

# Plot and embed in ipython notebook!
py.plot(data, filename='basic-line')


#######
# graph avg in 2nd bar graph
avg_dpm_snownobo = go.Bar(
    x=[0,1,2,3],
    y=avg_dpms[0],
    name='Snownobo'
)
avg_dpm_sky_fear = go.Bar(
    x=[0,1,2,3],
    y=avg_dpms[1],
    name='SKY Fear'
)
avg_dpm_liquid_fabbbyyy = go.Bar(
    x=[0,1,2,3],
    y=avg_dpms[2],
    name='Liquid Fabbbyyy'
)
avg_dpm_doublelift = go.Bar(
    x=[0,1,2,3],
    y=avg_dpms[3],
    name='Doublelift'
)
data = [avg_dpm_snownobo, avg_dpm_sky_fear, avg_dpm_liquid_fabbbyyy, avg_dpm_doublelift]

layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')