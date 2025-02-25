# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash
from dash import html

# Register the page
dash.register_page(__name__, path="/")

# Define the page layout
layout = html.Div([
    html.H1("About Filtera"),
    html.P("Welcome to the home page of our Dash app!")
])