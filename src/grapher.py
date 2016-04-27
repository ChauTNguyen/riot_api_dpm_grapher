import plotly.plotly as py
import plotly.graph_objs as go
from src.crawler import crawl, avg_dpms
from src.functions import get_summoner_id
region = "na"
# snownobo
snownobo_id = get_summoner_id(region, "snownobo")

dpm_snownobo = crawl(snownobo_id)

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
sky_fear_id = get_summoner_id(region, "skyfear")

dpm_sky_fear = crawl(sky_fear_id)

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
liquid_fabbbyyy_id = get_summoner_id(region, "liquidfabbbyyy")

dpm_liquid_fabbbyyy = crawl(liquid_fabbbyyy_id)

xs_liquid_fabbbyyy = []
for i in range(0, length): # same length as jynthe's
    xs_liquid_fabbbyyy.append(i)
trace_liquid_fabbbyyy = go.Scatter(
    x = xs_liquid_fabbbyyy,
    y = dpm_liquid_fabbbyyy,
    mode = "line + markers",
    name = "Liquid Fabbbyyy",
    line = dict(
        color=('rgb(255, 0, 0)'),
        width=2)
)

# doublelift
doublelift_id = get_summoner_id(region, "doublelift")

dpm_doublelift = crawl(doublelift_id)

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

# pecake
cake_id = get_summoner_id(region, "caaaaaaaaaaaaake")

dpm_cake = crawl(cake_id)

xs_cake = []
for i in range(0, length):
    xs_cake.append(i)
trace_cake = go.Scatter(
    x = xs_cake,
    y = dpm_cake,
    mode = "line + markers",
    name = "caaaaaaaaaaaaake",
    line = dict(
        color=('rgb(160, 32, 240'), #160-32-240
        width=2
    )
)

# rikara
rikara_id = get_summoner_id(region, "rikara")

dpm_rikara = crawl(rikara_id)

xs_rikara = []
for i in range(0, length):
    xs_rikara.append(i)

trace_rikara = go.Scatter(
    x=xs_rikara,
    y=dpm_rikara,
    mode="line + markers",
    name="Rikara",
    line=dict(
        color=('rgb(0, 50, 150'),  # 160-32-240
        width=2
    )
)

# array data
data = [trace_snownobo, trace_sky_fear, trace_liquid_fabbbyyy, trace_doublelift, trace_cake, trace_rikara]

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
avg_dpm_cake = go.Bar(
    x=[0,1,2,3],
    y=avg_dpms[4],
    name='caaaaaaaaaaaaake'
)
avg_dpm_rikara = go.Bar(
    x=[0,1,2,3],
    y=avg_dpms[5],
    name='Rikara'
)


# array data
data = [avg_dpm_snownobo, avg_dpm_sky_fear, avg_dpm_liquid_fabbbyyy, avg_dpm_doublelift, avg_dpm_cake, avg_dpm_rikara]

layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')