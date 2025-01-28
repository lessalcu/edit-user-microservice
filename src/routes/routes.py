from flask import request, jsonify
from src.models.models import db, User

# Route to edit user
def edit_user(id):
    try:
        # Get the data sent in the request body
        data = request.json
        # Find the user by their ID
        user = User.query.get(id)

        # Check if the user exists
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Update user data
        if 'identification' in data:
            user.identification = data['identification']
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']
        if 'type' in data:
            user.type = data['type']

        # Save changes to the database
        db.session.commit()

        return jsonify({'mensaje': 'Usuario actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400