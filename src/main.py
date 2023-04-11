from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages.home import create_page_home
from src.pages.page_2 import create_page_2
from src.pages.page_3 import create_page_3
import dash
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return create_page_2()
    if pathname == '/page-3':
        return create_page_3()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)
