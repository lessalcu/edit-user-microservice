from flask import Flask
from flask_cors import CORS
from src.config.config import Config
from src.models.models import db
from src.routes.routes import edit_user

# Create the application
app = Flask(__name__)

CORS(app)

# Configure the application
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the edit user route
@app.route('/users/<int:id>', methods=['PUT'])
def edit_user_route(id):
    return edit_user(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
