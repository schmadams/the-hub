from src.templates.populations.main_layout import page_template
from src.pipelines.load.populations import LoadPopulations
from src.helper_functions.helpers import data_table_content
from dash import callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

prefix = 'populations-'

def populations_layout():
    return page_template(prefix=prefix)

@callback(
    Output(f'{prefix}populations-data', 'data'),
    Input(f'{prefix}page', 'children'),
)
def load_populations_table_data(trigger):
    data = LoadPopulations().data
    return data

@callback(
    Output(f'{prefix}populations-dropdown',  'options'),
    Output(f'{prefix}populations-dropdown',  'value'),
    Input(f'{prefix}populations-data', 'data'),
    State(f'{prefix}populations-dropdown', 'value'),
    prevent_initial_call=True
)
def populations_granularity_dropdown(pop_data, selected_gran):
    if None in (pop_data):
        raise PreventUpdate

    options = [
        {'label': 'Full SIC Code (5 digits)', 'value': 'sic'},
        {'label': 'Section (Least Granular Category)', 'value': 'section'},
        {'label': 'Division (First 2 digits)', 'value': 'division'},
        {'label': 'Group (First 3 digits)', 'value': 'group'}
    ]
    options = [x for x in options if x['value'] != selected_gran]
    return options, selected_gran

@callback(
    Output(f'{prefix}populations-table', 'data'),
    Output(f'{prefix}populations-table', 'columns'),
    Output(f'{prefix}populations-table-container', 'hidden'),
    Input(f'{prefix}populations-dropdown', 'value'),
    State(f'{prefix}populations-data', 'data'),
    prevent_initial_call=True
)
def populate_populations_table(selected, data):
    print(selected)
    if selected == 'section':
        table_df = pd.DataFrame(data['section_pops'])[['section_description', 'section', 'count', '%_of_total']]
        table_data, columns = data_table_content(data=table_df)
        hidden = False
    elif selected == 'division':
        table_df = pd.DataFrame(data['division_pops'])[['division_description', 'division', 'count', '%_of_total']]
        table_data, columns = data_table_content(data=table_df)
        hidden = False
    elif selected == 'sic':
        table_df = pd.DataFrame(data['sic_pops'])[['sic_description', 'sic', 'count', '%_of_total']]
        table_data, columns = data_table_content(data=table_df)
        hidden = False
    else:
        table_data, columns, hidden = None, None, True
    return table_data, columns, hidden