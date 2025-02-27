# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc  # Import Dash Bootstrap Components
import datetime

# Register the page
dash.register_page(__name__, path="/film")

# Define the page layout and content
layout = html.Div([
    dbc.Row([
        # Sidebar
        dbc.Col([
            html.H4("Genres"),
            dbc.ButtonGroup(
                [
                    dbc.Button("Action", color="primary", href="/action", active=True),  # Make this button active by default
                    dbc.Button("Fantasy", color="primary", href="/fantasy"),
                    dbc.Button("Drama", color="primary", href="/drama"),
                    dbc.Button("Sci-Fi", color="primary", href="/sci-fi"),
                ],
                vertical=True,
                className="me-2"
            ),
        ], width=2, style={"border-right": "1px solid rgb(34, 34, 34)", "padding": "20px"}),

        # Main content
        dbc.Col([
            html.P("Interactively explore film data using tables and visualizations."),
            html.Div(id="content-area")  # This is where the content will be displayed
        ], width=10)
    ])
],

# Styling the content region
style={
        "border": "1px solid rgb(34, 34, 34)",  # Black border with 1px width
        "padding": "20px",  # Padding inside the box
        "border-radius": "0px",  # Unrounded corners
        "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)"  # A shadow for better visual effect
    }
)