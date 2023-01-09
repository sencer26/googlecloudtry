import numpy as np
import pandas as pd
import panel as pn
import plotly.express as px
from holoviews.selection import link_selections
from holoviews import opts

import hvplot.pandas

pn.extension(sizing_mode="stretch_width")

DAY_TO_INT = {"Thur": 4, "Fri": 5, "Sat": 6, "Sun": 7,}
DAY_TICKS = [(val, key) for key, val in DAY_TO_INT.items()]
HEIGHT = 400
TOOLS = dict(tools=["hover"], active_tools=["box_select"])


def load_dataset():
    df = px.data.tips()
    df["count"] = 1
    df["size"] = df["size"].astype(str)
    df["day_int"] = df["day"].map(DAY_TO_INT)
    return df

df = pn.state.as_cached("tips", load_dataset)

bill_to_tip_figure = df.hvplot.scatter(
    x="total_bill", y="tip", responsive=True
)
day_figure = df.hvplot.hist(
    "day_int", xlabel="day", ylabel="number of orders", responsive=True
).opts(xticks=DAY_TICKS)
size_to_time_figure = df.sort_values("size").hvplot.heatmap(
    x="size", y="time", C="count", reduce_function=np.sum, colorbar=False, responsive=True
)

selections = link_selections.instance()
bill_to_tip_figure = selections(bill_to_tip_figure).opts(**TOOLS)
day_figure = selections(day_figure).opts(**TOOLS)
size_to_time_figure = selections(size_to_time_figure).opts(**TOOLS)

template = pn.template.FastGridTemplate(
    site="Awesome Panel", title="Interactive Data Exploration w. Cross Filtering",
    row_height=125,  prevent_collision=True, save_layout=True,
)
template.main[0:3,0:12]=pn.pane.HoloViews(bill_to_tip_figure, sizing_mode="stretch_both")
template.main[3:6,0:6]=pn.pane.HoloViews(day_figure, sizing_mode="stretch_both")
template.main[3:6,6:12]=pn.pane.HoloViews(size_to_time_figure, sizing_mode="stretch_both")
template.servable();
