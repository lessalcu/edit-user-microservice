from flask import request, jsonify
from models import db, User

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
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']
        
        # Save changes to database
        db.session.commit()

        return jsonify({'mensaje': 'Usuario actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
