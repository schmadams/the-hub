from src.templates.populations.populations_features import page_layout
from dash import html
import dash_core_components as dcc
def page_template(prefix):
    make_storages(prefix)
    layout = html.Div(id=f'{prefix}page', children=page_layout(prefix))
    return layout

def make_storages(prefix):
    content = [
        dcc.Store(id=f'{prefix}pop-data-1', storage_type='memory')
    ]
    return content