from flask import Flask
from controllers import user_controller, file_controller
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

# Create a Flask application
app = Flask(__name__)

# routers
app.register_blueprint(user_controller.user_blueprint)
app.register_blueprint(file_controller.file_blueprint)


@app.route('/')
def hello_world():
    return 'server is running'


load_dotenv()
cors = CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
