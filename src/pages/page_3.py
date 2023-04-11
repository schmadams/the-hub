from dash import html
from src.helper_functions.navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to page 3!')


def create_page_3():
    layout = html.Div([
        nav,
        header,
    ])
    print(layout.children)
    return layout
