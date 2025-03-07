# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash
import dash_bootstrap_components as dbc
from navbar import navbar
from dash import html

# Add Bootstrap and FontAwesome
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
    "/assets/styles.css"
]

# Initialize the Dash app
app = dash.Dash(__name__, use_pages=True, 
                external_stylesheets=external_stylesheets, 
                suppress_callback_exceptions=True)

# Layout - This is the only layout needed
app.layout = dbc.Container([
    navbar,  # Navigation bar
    dbc.Row([dbc.Col(dash.page_container, width=12)]),  # Loads the correct page

    # Footer
    html.Footer(
        "© 2025 Cornelius Tanui. All rights reserved.",
        style={
            "position": "fixed", # Ensure the footer is always at the bottom of the page
            "left": "0", 
            "bottom": "0",
            "width": "100%",
            "text-align": "center",
            "padding": "10px",
            "border-top": "1px solid rgba(34, 34, 34, 0.1)", # Add a faint border at the top
            "background-color": "white"  # Ensure the footer has a background color
        }
    )

], fluid=True)

# Expose the server for deployment
server = app.server

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
