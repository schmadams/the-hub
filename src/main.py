from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages.home import create_page_home
from src.pages.populations import create_page_template
from src.pages.page_3 import create_page_3
import dash
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, suppress_callback_exceptions=False, external_stylesheets=[dbc.themes.LUX])

server = app.server
app.config.suppress_callback_exceptions = False

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/populations':
        print('running pop page')
        return create_page_template()
    if pathname == '/page-3':
        return create_page_3()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)
