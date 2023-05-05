from src.helper_functions.navbar import create_navbar
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
from src.helper_functions.datatables_builder import PopulationsTables

def top_left_container(prefix):
    return html.Div(className='column', children=[
        html.Div(className='row', children=[
            html.H3('SIC Granularity Populations',
                    style={'width': '15vw', 'text-align': 'center', 'color': 'white', 'margin': 'auto'}),
            dcc.Dropdown(id=f'{prefix}populations-dropdown', multi=False,
                         style={'width': '15vw', 'margin': 'auto'})
        ], style={'width': '40vw', 'margin': 'auto'}),
        html.Div(id=f'{prefix}populations-table-container', children=[
            PopulationsTables(prefix).populatiions_granularity_table()
        ], hidden=True, style={'margin': 'auto'})
    ], style={'width': '45vw', 'height': '25vw', 'margin': 'auto',
              'border-radius': '25px', 'background': '#171049'})

def top_right_container(prefix):
    return html.Div(className='column', children=[
        html.Div(className='row', children=[
            html.H3('Entity Type Populations',
                    style={'width': '15vw', 'text-align': 'center', 'color': 'white', 'margin': 'auto'})
        ], style={'width': '40vw', 'margin': 'auto'}),
        html.Div(id=f'{prefix}entities-table-container', children=[
            PopulationsTables(prefix).populations_entities_table()
        ], hidden=True, style={'margin': '1vw 1vw'})
    ], style={'width': '45vw', 'height': '25vw', 'margin': 'auto',
              'border-radius': '25px', 'background': '#171049'})


def page_layout(prefix):
    content = [
        create_navbar(),
        html.H1('Populations', style={'text-align': 'center', 'margin': '1vw', 'color': 'white'}),
        html.Div(className='row', children=[
            top_left_container(prefix),
            top_right_container(prefix)
        ]),
        html.Div(id=f'{prefix}treemap_container', children=[
            dcc.Graph(id=f'{prefix}treemap', style={'width': '90vw', 'height': '50vw', 'margin': 'auto'})
        ], hidden=True, style={'background': '#171049', 'border-radius': '25px', 'width': '90vw', 'margin': '2vw auto'})
    ]
    return content











#