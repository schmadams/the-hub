from dash import html, dcc, dash_table


class PopulationsTables:
    def __init__(self, prefix):
        self.prefix = prefix
    def populatiions_granularity_table(self):
        return dash_table.DataTable(
            id=f'{self.prefix}populations-table',
            style_data={'whiteSpace': 'normal', 'backgroundColor': '#171049', 'color': 'white', 'border': 'none'},
            style_header={'textAlign': 'center', 'backgroundColor': '#470A68', 'color': 'white'},
            style_cell={'textAlign': 'center', 'fontSize': 12, 'font-family': 'sans-serif', 'minWidth': '100px'},
            style_table={'overflowY': 'auto', 'height': '18vw'},
            sort_action="native",
            style_as_list_view=True,
            css=[
                {"selector": ".dash-spreadsheet tr th", "rule": "height: 5px;"},  # set height of header
                {"selector": ".dash-spreadsheet tr td", "rule": "height: 5px;"},  # set height of body rows
            ]
        )

    def populations_entities_table(self):
        return dash_table.DataTable(
            id=f'{self.prefix}populations-entities-table',
            style_data={'whiteSpace': 'normal', 'backgroundColor': '#171049', 'color': 'white', 'border': 'none'},
            style_header={'textAlign': 'center', 'backgroundColor': '#470A68', 'color': 'white'},
            style_cell={'textAlign': 'center', 'fontSize': 12, 'font-family': 'sans-serif', 'minWidth': '100px'},
            style_table={'overflowY': 'auto', 'height': '18vw'},
            sort_action="native",
            style_as_list_view=True,
            css=[
                {"selector": ".dash-spreadsheet tr th", "rule": "height: 5px;"},  # set height of header
                {"selector": ".dash-spreadsheet tr td", "rule": "height: 5px;"},  # set height of body rows
            ]
        )