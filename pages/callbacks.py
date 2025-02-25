# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

# Function to display the page content
def display_page(pathname):
    return render_page_content(pathname)
