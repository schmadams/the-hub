import sys
import dash_bootstrap_components as dbc
from src.helper_functions.helpers import load_nav_logo
from pathlib import Path
from dash import html, get_asset_url
from PIL import Image
import importlib


def create_navbar():
    nav_item = dbc.NavItem(dbc.NavLink("Home", href="/home"))
    dropdown = dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Menu",
                    children=[
                        dbc.DropdownMenuItem("Home", href='/home'),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem("Populations", href='/populations'),
                        dbc.DropdownMenuItem("International Transactions", href='/international_transactions'),
                    ],
                )

    logo = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=Image.open(load_nav_logo()), height="80px", width='80px')),
                        ],
                        align="left",
                        className="g-0",
                    ),
                    href="https://kpmg.com/xx/en/home.html",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [nav_item, dropdown],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                ),
            ],
        ),
        color="#00338D",
        dark=True,
        sticky="top",
        className="mb-5",
        style={'height': '80px'}
    )
    return logo

if __name__ == '__main__':
    load_nav_logo()
