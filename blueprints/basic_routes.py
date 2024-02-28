from flask import Blueprint, render_template
import os, sys
from utils import generation as gen

sys.path.append('utils')
basic_route = Blueprint('basic_route', __name__)

# == DEFINE THE ROUTES HERE ==
@basic_route.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@basic_route.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@basic_route.route('/appointment', methods = ['GET'])
def appointment():
    return render_template('appointment.html')

@basic_route.route('/contact', methods = ['GET'])
def contact():
    return render_template('contact.html')

@basic_route.route('/feature', methods = ['GET'])
def feature():
    return render_template('feature.html')

@basic_route.route('/service', methods = ['GET'])
def service():
    return render_template('service.html')

@basic_route.route('/team', methods = ['GET'])
def team():
    return render_template('team.html')

@basic_route.route('/testimonial', methods = ['GET'])
def testimonial():
    return render_template('testimonial.html')