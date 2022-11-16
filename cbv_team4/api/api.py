from flask import Flask
from flask_cors import CORS

# Other python files which contain other routes that are needed
from packet_receiver import packet_receiver
from project_configuration import project_configuration
from node_manager import node_manager
from syncronizer import syncronizer

# Main app and the other files that contain the other routes
app = Flask(__name__)
app.register_blueprint(packet_receiver)
app.register_blueprint(project_configuration)
app.register_blueprint(syncronizer)
# app.register_blueprint(node_manager)
CORS(app)
#TODO: make sure backend is killed with scripts
'''
Description: At localhost:5000/ 
@return: str: default response of backend server.
'''
@app.route("/")
def home_page():
    return "Hey you! The backend server is up and running :)"