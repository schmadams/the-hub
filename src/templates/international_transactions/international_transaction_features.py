from src.helper_functions.navbar import create_navbar
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc


def page_layout(prefix):
    content = [
        create_navbar(),
        html.H1('International Transactions', style={'text-align': 'center', 'margin': '1vw', 'color': 'white'}),
        html.Div(className='row', children=[
        ]),
    ]
    return content
