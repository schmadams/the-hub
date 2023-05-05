from dash import callback, Input, Output, State
from dash.exceptions import PreventUpdate
from src.templates.international_transactions.main_layout import page_template
import pandas as pd

prefix = 'international_transactions-'

def international_transactions_layout():
    return page_template(prefix=prefix)
