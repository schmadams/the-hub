from dash import html
from src.helper_functions.navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to home page!')


def create_page_home():
    layout = html.Div(children=[
        nav,
        header,
    ])
    return layout
