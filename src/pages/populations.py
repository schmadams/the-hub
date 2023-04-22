from src.templates.populations.main_layout import page_template
from src.pipelines.load.populations import LoadPopulations
from src.helper_functions.helpers import data_table_content, load_config
from src.helper_functions.plot_building import build_treemap
from src.pipelines.transform.populations import TreeMapDescriptions
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
    elif selected == 'group':
        table_df = pd.DataFrame(data['group_pops'])[['group_description', 'group', 'count', '%_of_total']]
        table_data, columns = data_table_content(data=table_df)
        hidden = False
    else:
        table_data, columns, hidden = None, None, True
    return table_data, columns, hidden


@callback(
    Output(f'{prefix}treemap', 'figure'),
    Output(f'{prefix}treemap_container', 'hidden'),
    Input(f'{prefix}populations-data', 'data'),
    prevent_initial_call=True
)
def sic_heirarchy_treemap(data):
    print('trigger tree')
    if None in data:
        raise PreventUpdate

    data = pd.DataFrame(data['companies'])
    desc_adder = TreeMapDescriptions()
    data = desc_adder.add_section_description(data)
    data = desc_adder.add_division_description(data)
    data = desc_adder.add_group_description(data)
    data = desc_adder.add_sic_description(data)
    fig = build_treemap(data, cols=['section_description', 'division_description', 'group_description', 'sic_description'])
    hidden = False
    return fig, hidden


@callback(
    Output(f'{prefix}populations-entities-table', 'data'),
    Output(f'{prefix}populations-entities-table', 'columns'),
    Output(f'{prefix}entities-table-container', 'hidden'),
    Input(f'{prefix}populations-data', 'data'),
    State(f'{prefix}populations-data', 'data'),
    prevent_initial_call=True
)
def populate_entities_table(selected, data):
    if None in [data]:
        raise PreventUpdate

    table_data = pd.DataFrame(data['companies'])
    table_data = table_data.groupby(['entity_type']).size().reset_index(name='count')
    table_data, columns = data_table_content(data=table_data)
    hidden = False

    return table_data, columns, hidden