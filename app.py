from flask import Flask
from config import Config
from models import db
from routes import edit_user

# Create the application
app = Flask(__name__)

# Configure the application
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the edit user route
@app.route('/users/<int:id>', methods=['PUT'])
def edit_user_route(id):
    return edit_user(id)

if __name__ == '__main__':
    app.run(debug=True)