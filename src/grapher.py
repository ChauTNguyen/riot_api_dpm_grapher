import plotly.plotly as py
import plotly.graph_objs as go
from src.crawler import crawl, avg_dpms
from src.functions import get_summoner_id
from time import sleep

REGION = "na"


def graph_dpm():
    def get_trace(name, config):
        id = get_summoner_id(REGION, name)
        sleep(2)
        xs = []             # game #'s
        ys = crawl(id)      # dpm's

        for i in range(0, len(ys)):
            xs.append(i)

        return go.Scatter(x=xs, y=ys, mode=config[0], name=name, line=config[2])

    scatter_mode = "line + markers"

    p1_name = "apoiloprice"
    p2_name = "rikara"
    p3_name = "mvsh"
    p4_name = "envynien"
    p5_name = "envylod"
    p6_name = "skyfear"
    p7_name = "tm8"

    p1_config = (scatter_mode, p1_name, dict(color=('rgb(0, 255, 0)'), width=2))
    p2_config = (scatter_mode, p2_name, dict(color=('rgb(0, 50, 150'), width=2))
    p3_config = (scatter_mode, p3_name, dict(color=('rgb(20, 90, 30'), width=2))
    p4_config = (scatter_mode, p4_name, dict(color=('rgb(92, 42, 120'), width=2))
    p5_config = (scatter_mode, p5_name, dict(color=('rgb(123, 91, 32'), width=2))
    p6_config = (scatter_mode, p6_name, dict(color=('rgb(232, 92, 10)'), width=2))
    p7_config = (scatter_mode, p7_name, dict(color=('rgb(23, 150, 203'), width=2))

    p1 = get_trace(p1_name, p1_config)
    p2 = get_trace(p2_name, p2_config)
    p3 = get_trace(p3_name, p3_config)
    p4 = get_trace(p4_name, p4_config)
    p5 = get_trace(p5_name, p5_config)
    p6 = get_trace(p6_name, p6_config)
    p7 = get_trace(p7_name, p7_config)

    data = [p1, p2, p3, p4, p5, p6, p7]
    py.plot(data, filename='basic-line')


def graph_avg_dpm():
    def get_trace(name, index):
        sleep(2)
        xs = []  # game #'s

        for i in range(0, len(avg_dpms)):
            xs.append(i)

        return go.Bar(x=xs, y=avg_dpms[index], name=name)

    p1_name = "apoiloprice"
    p2_name = "rikara"
    p3_name = "mvsh"
    p4_name = "envynien"
    p5_name = "envylod"
    p6_name = "skyfear"
    p7_name = "tm8"

    p1 = get_trace(p1_name, 0)
    p2 = get_trace(p2_name, 1)
    p3 = get_trace(p3_name, 2)
    p4 = get_trace(p4_name, 3)
    p5 = get_trace(p5_name, 4)
    p6 = get_trace(p6_name, 5)
    p7 = get_trace(p7_name, 6)

    fig = go.Figure(data=[p1, p2, p3, p4, p5, p6, p7], layout=go.Layout(barmode='group'))
    py.plot(fig, filename='grouped-bar')


if __name__ == '__main__':
    graph_dpm()
    graph_avg_dpm()