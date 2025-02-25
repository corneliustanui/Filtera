# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
from dash import dcc, html, Input, Output, callback
from app import app  # Import your Dash app instance
from pages import render_page_content  # Ensure this function is correctly imported

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

# Function to display the page content
def display_page(pathname):
    return render_page_content(pathname)


