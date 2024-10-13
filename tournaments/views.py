from flask import Blueprint, render_template

# Define a Blueprint named 'main' to organize routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')  

@main.route('/createEvent')
def createEvent():
    return render_template('createEvent.html') 


@main.route('/eventDetails')
def eventDetails():
    return render_template('eventDetails.html') 


@main.route('/history')
def history():
    return render_template('history.html') 

