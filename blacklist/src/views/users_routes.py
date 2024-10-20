from flask import Flask, jsonify, request, Blueprint
from ..models.model import Blacklist,db
from flask_jwt_extended import  jwt_required, create_access_token

user_blueprint = Blueprint('user', __name__)
    
# endpoint login
@user_blueprint.route('/login/auth', methods=['POST'])
def login_generate_token():

    access_token = create_access_token(identity='test_user')
    return jsonify(access_token=access_token), 200

# endpoint get info user
@user_blueprint.route('/blacklists', methods=['POST'])
@jwt_required()
def add_email_to_blacklist():
    data = request.get_json()

    # Validar los datos recibidos
    email = data.get('email')
    app_uuid = data.get('app_uuid')
    blocked_reason = data.get('blocked_reason', '')

    # Verificar si el email ya existe en la lista negra
    if Blacklist.query.filter_by(email=email).first():
        return jsonify({'message': 'Email is already in the blacklist'}), 400

    # Obtener la IP del solicitante
    ip_address = request.remote_addr

    # Crear un nuevo registro en la lista negra
    new_blacklist_entry = Blacklist(
        email=email,
        app_uuid=app_uuid,
        blocked_reason=blocked_reason,
        ip_address=ip_address
    )
    db.session.add(new_blacklist_entry)
    db.session.commit()

    return jsonify({'message': 'Email added to blacklist'}), 201


# endpoint reset DB
@user_blueprint.route('/blacklists/<string:email>', methods=['GET'])
@jwt_required()
def check_email_in_blacklist(email):
    
    # Buscar si el email está en la lista negra
    blacklist_entry = Blacklist.query.filter_by(email=email).first()

    if blacklist_entry:
        return jsonify({
            'email': email,
            'in_blacklist': True,
            'blocked_reason': blacklist_entry.blocked_reason
        }), 200
    else:
        return jsonify({'email': email, 'in_blacklist': False}), 404


# endpoint health check service
@user_blueprint.route('/users/ping', methods=['GET'])
def ping():
    return 'pong', 200

