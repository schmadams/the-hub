import plotly_express as px
import pandas as pd
from plotly.graph_objs import *


def build_treemap(data, cols):
    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    tree_data = data.groupby(cols).size().reset_index(name='population')
    cols = [px.Constant('all customers')] + cols
    fig = px.treemap(tree_data, path=cols, values='population').update_layout(layout)
    fig.update_traces(hovertemplate='labels=%{label}<br>population=%{value}<br>parent=%{parent}')
    fig.data[0]['textfont']['color'] = "white"
    return fig

