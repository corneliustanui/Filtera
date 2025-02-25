# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash_bootstrap_components as dbc
from dash import dcc

# Define the Navbar
navbar = dbc.NavbarSimple(
    brand="Filtera",
    brand_href="/",
    color="#4D4D4F",
    dark=True,
    children=[
        dbc.NavItem(dcc.Link("About", href="/", className="nav-link text-titlecase fw-light fs-5 text-white")),
        dbc.NavItem(dcc.Link("Film", href="/film", className="nav-link text-titlecase fw-light fs-5 text-white")),
        dbc.NavItem(dcc.Link("Literature", href="/literature", className="nav-link text-titlecase fw-light fs-5 text-white")),

        # The main dropdown link text
        dbc.DropdownMenu(
            className="nav-link text-titlecase fw-light fs-5 text-white",
            style={'margin': "0px", 'padding': "0px"},
            label="Contact",
            nav=True,
            in_navbar=True,
            children=[
                dbc.DropdownMenuItem("GitHub", href="https://github.com/corneliustanui", external_link=True),
                dbc.DropdownMenuItem("LinkedIn", href="https://ke.linkedin.com/in/cornelius-tanui-527979b9", external_link=True)
            ]
        ),
    ],
    # fluid=True, # Make the Navbar fluid
    style={"height": "30%", "width": "100%", 'margin': "0px", 'padding': "0px"}
)