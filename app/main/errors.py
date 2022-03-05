from flask import render_template
from app import app

@app.errorhandler(404)
def error_page (errors):
    '''
    Function to render the 404 error page
    '''
    return render_template('error_page.html'),404 