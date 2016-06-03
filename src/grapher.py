import plotly.plotly as py
import plotly.graph_objs as go
from src.crawler import crawl, avg_dpms
from src.functions import get_summoner_id
from time import sleep

REGION = "na"
players = ['apoiloprice', 'rikara', 'mvsh', 'envynien', 'envylod', 'skyfear', 'tm8']

def graph_dpm():
    def get_trace(name, config):
        id = get_summoner_id(REGION, name)
        sleep(2)
        xs = []             # game #'s
        ys = crawl(id)      # dpm's

        for i in range(0, len(ys)):
            xs.append(i)

        return go.Scatter(x=xs, y=ys, mode=config[0], name=name, line=config[1])

    scatter_mode = "line + markers"

    configs = [
        (scatter_mode, dict(color=('rgb(0, 255, 0)'), width=2)),
        (scatter_mode, dict(color=('rgb(0, 50, 150'), width=2)),
        (scatter_mode, dict(color=('rgb(20, 90, 30'), width=2)),
        (scatter_mode, dict(color=('rgb(92, 42, 120'), width=2)),
        (scatter_mode, dict(color=('rgb(123, 91, 32'), width=2)),
        (scatter_mode, dict(color=('rgb(232, 92, 10)'), width=2)),
        (scatter_mode, dict(color=('rgb(23, 150, 203'), width=2))
    ]

    traces = []
    for i in range(0, len(players)):
        traces.append(get_trace(players[i], configs[i]))

    py.plot(traces, filename='basic-line')


def graph_avg_dpm():
    def get_trace(name, index):
        sleep(2)
        xs = []  # game #'s

        for i in range(0, len(avg_dpms)):
            xs.append(i)

        return go.Bar(x=xs, y=avg_dpms[index], name=name)

    traces = []

    for i in range(0, len(players)):
        traces.append(get_trace(players[i], i))

    fig = go.Figure(data=traces, layout=go.Layout(barmode='group'))
    py.plot(fig, filename='grouped-bar')


if __name__ == '__main__':
    graph_dpm()
    graph_avg_dpm()