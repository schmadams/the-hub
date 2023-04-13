from dash import html, dcc, dash_table


class PopulationsTables:
    def __init__(self, prefix):
        self.prefix = prefix
    def populatiions_granularity_table(self):
        return dash_table.DataTable(
            id=f'{self.prefix}populations-table',
            style_data={'whiteSpace': 'normal'},
            style_header={'textAlign': 'center', 'backgroundColor': '#470A68', 'color': 'white'},
            style_cell={'textAlign': 'left', 'fontSize': 15, 'font-family': 'sans-serif', 'minWidth': '100px'},
            style_table={'overflowY': 'auto', 'height': '20vw', 'borderRadius': '15px'},
            sort_action="native"
        )