from src.helper_functions.navbar import create_navbar
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc

def risk_grid(prefix):
    return html.Div(className='flex-row', id=f'{prefix}monitoring-risk-grid', style={'margin': 'auto'})


def page_layout(prefix):
    content = [
        create_navbar(),
        html.H1('Risk Monitoring', style={'text-align': 'center', 'margin': '1vw', 'color': 'white'})
    ]
    return content




