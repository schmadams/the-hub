from src.templates.populations.main_layout import page_template
from dash import callback
prefix = 'populations-'

def create_page_template():
    return page_template(prefix=prefix)

# @callback(
#
# )
# def load_populations_table_data():