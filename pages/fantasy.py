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
dash.register_page(__name__, path="/fantasy")

# Define the page layout and content
layout = html.Div([
    dbc.Row([
        dbc.Col([

            # content
            html.P("Show some fantasy!"),
        ])
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
