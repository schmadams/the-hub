from src.helper_functions.navbar import create_navbar
from dash import html

def page_layout(prefix):
    content = [
        create_navbar(),
        html.H3('populations')
        ]
    print('created layout')
    return content











#