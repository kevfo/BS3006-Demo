from flask import Flask
from blueprints.basic_routes import basic_route 

app = Flask(__name__)
app.register_blueprint(basic_route)

if __name__ == '__main__':
    app.run(debug = True)