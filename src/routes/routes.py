import os
import requests
from flask import request, jsonify
from src.models.models import db, User
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL del microservicio de consulta
QUERY_MICROSERVICE_URL = os.getenv('QUERY_MICROSERVICE_URL')

def edit_user(id):
    try:
        data = request.json  

      
        response = requests.get(f'{QUERY_MICROSERVICE_URL}/{id}')
        if response.status_code != 200:
            return jsonify({'error': 'User not found'}), 404

        user_data = response.json()  


        if 'identification' in data:
            user_data['identification'] = data['identification']
        if 'name' in data:
            user_data['name'] = data['name']
        if 'email' in data:
            user_data['email'] = data['email']
        if 'type' in data:
            user_data['type'] = data['type']

     
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found in database'}), 404

       
        if 'password' in data and data['password']:
            user.set_password(data['password'])

        user.identification = user_data['identification']
        user.name = user_data['name']
        user.email = user_data['email']
        user.type = user_data['type']

        db.session.commit()

        return jsonify({'message': 'User updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400
