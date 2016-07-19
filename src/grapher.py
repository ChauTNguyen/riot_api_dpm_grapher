import plotly.graph_objs as go
import plotly.plotly as py

from src.crawler import crawl_dpm, crawl_avg_dpm
from src.functions import get_summoner_id

player_names = ['apoiloprice', 'rikara', 'mvsh', 'envynien', 'envylod', 'skyfear', 'tm8']
avg_dpms = []


def graph_dpm():
    def get_trace(name, config):
        id = get_summoner_id(name)
        xs = [i for i in range(0, len(player_names))]  # game #'s
        ys = crawl_dpm(id)  # dpm's
        print(name + "'s analysis completed.\n")
        return go.Scatter(x=xs, y=ys, mode=config[0], name=name, line=config[1])

    scatter_mode = 'line + markers'

    configs = [
        (scatter_mode, dict(color=('rgb(182, 190, 220'), width=2)),
        (scatter_mode, dict(color=('rgb(0, 255, 0)'), width=2)),
        (scatter_mode, dict(color=('rgb(0, 50, 150'), width=2)),
        (scatter_mode, dict(color=('rgb(20, 90, 30'), width=2)),
        (scatter_mode, dict(color=('rgb(92, 42, 120'), width=2)),
        (scatter_mode, dict(color=('rgb(123, 91, 32'), width=2)),
        (scatter_mode, dict(color=('rgb(232, 92, 10)'), width=2)),
        (scatter_mode, dict(color=('rgb(23, 150, 203'), width=2)),
        (scatter_mode, dict(color=('rgb(1200, 90, 30'), width=2))
    ]

    traces = [(get_trace(player_names[i], configs[i])) for i in range(0, len(player_names))]
    py.plot(traces, filename='basic-line')


def graph_avg_dpm():  # separated the functions (calls many more api requests though if both are run ofc)
    def get_trace(name, index):
        id = get_summoner_id(name)
        xs = [i for i in range(0, len(player_names))]  # game #'s
        avg_dpms.append(crawl_avg_dpm(id))
        ys = avg_dpms[index]

        print(name + "'s analysis completed.")
        return go.Bar(x=xs, y=ys, name=name)

    traces = [(get_trace(player_names[i], i)) for i in range(0, len(player_names))]
    fig = go.Figure(data=traces, layout=go.Layout(barmode='group'))
    py.plot(fig, filename='grouped-bar')


if __name__ == '__main__':
    graph_dpm()
    graph_avg_dpm()
