import os
import requests
from flask import request, jsonify
from src.models.models import db, User
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the microservice URL from environment variables
QUERY_MICROSERVICE_URL = os.getenv('QUERY_MICROSERVICE_URL')

# Route to edit user
def edit_user(id):
    try:
        # Get the data sent in the request body
        data = request.json

        # Make a request to the microservice to get the user by their ID
        response = requests.get(f'{QUERY_MICROSERVICE_URL}/{id}')
        
        # Check if the user exists
        if response.status_code != 200:
            return jsonify({'error': 'User not found'}), 404

        user_data = response.json()

        # Update user data
        if 'identification' in data:
            user_data['identification'] = data['identification']
        if 'name' in data:
            user_data['name'] = data['name']
        if 'email' in data:
            user_data['email'] = data['email']
        if 'password' in data:
            user_data['password'] = data['password']
        if 'type' in data:
            user_data['type'] = data['type']

        # Save changes to the database
        user = User.query.get(id)
        if user:
            user.identification = user_data['identification']
            user.name = user_data['name']
            user.email = user_data['email']
            user.password = user_data['password']
            user.type = user_data['type']
            db.session.commit()

        return jsonify({'mensaje': 'User updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400