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

# register the page
dash.register_page(__name__, path="/about")

# page layout
layout = html.Div([
    html.H1("Filtera"),
    html.P("This is the About page. Learn more about our app.")
])