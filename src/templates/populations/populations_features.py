from src.helper_functions.navbar import create_navbar
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
from src.helper_functions.datatables_builder import PopulationsTables

def page_layout(prefix):
    content = [
        create_navbar(),
        html.H1('Populations', style={'text-align': 'center', 'margin': '1vw'}),
        html.Div(className='flex-row', children=[
            html.Div(className='column', children=[
                html.H3('SIC Granularity Populations', style={'text-align': 'center', 'margin': '1vw'}),
                dcc.Dropdown(id=f'{prefix}populations-dropdown', multi=False,
                             style={'width': '15vw', 'margin': '1vw auto'}),
                html.Div(id=f'{prefix}populations-table-container', children=[
                    PopulationsTables(prefix).populatiions_granularity_table()
                ], hidden=True, style={'margin': '1vw 1vw'})
            ], style={'width': '45vw', 'height': '30vw', 'margin': '2vw 3vw',
                      'border-radius': '25px', 'border': '2px solid #6D2077', 'background': '#E9E8E8'})
        ])
        ]
    return content











#