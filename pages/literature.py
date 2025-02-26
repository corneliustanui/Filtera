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
dash.register_page(__name__, path="/literature")


layout = html.Div([
    dbc.Row([
        dbc.Col([
            # bigger text
            html.H1("Dash App Demo!"),

            # smaller text
            html.P("This is a basic Dash app to demonstrate components and deployment.")])])])
