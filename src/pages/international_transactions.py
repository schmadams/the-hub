from dash import callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

prefix = 'populations-'

def populations_layout():
    return page_template(prefix=prefix)



def create_page_3():
    layout = html.Div([
        nav,
        header,
    ])
    print(layout.children)
    return layout
