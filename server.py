from flask import Flask, request, jsonify
from data import add_spaceship, get_spaceships_list, get_spaceship_by_id, update_spaceship_status, check_status, delete_spaceship
from schemas import SpaceshipSchema, SpaceshipUpdateSchema
from marshmallow import ValidationError

app = Flask(__name__)

@app.get('/api/v1/spaceships')
def get_spaceships_list_controller():
    return get_spaceships_list(), 200

@app.get('/api/v1/spaceships/<id>')
def get_spaceship_by_id_controller(id: str):
    spaceship = get_spaceship_by_id(id)
    if spaceship is None:
        return {"error": "Spaceship not found"}, 404
    return jsonify(spaceship), 200


@app.post('/api/v1/spaceships')
def create_spaceship_controller():
    schema = SpaceshipSchema()
    if request.json is None:
        return {"error": "No JSON provided"}, 400
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return {"error": err.messages}, 400
    if not data or not isinstance(data, dict):
     return {"error": "Wrong data format"}, 400
    try:
        new_ship = add_spaceship(data['name'], data['type_'], data.get('status', 'available'))
    except ValueError as err:
        return {"error": str(err)}, 400
    result = schema.dump(new_ship)
    return jsonify(result), 201


@app.patch('/api/v1/spaceships/<id>')
def update_status_controller(id: str):
    if request.json is None:
        return {'error': 'No JSON provided'}, 400
    
    schema = SpaceshipUpdateSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return {'error': err.messages}, 400
    if not data or not isinstance(data, dict):
        return {'error': 'Wrong data format'}, 400
    
    new_status = data['status']
    try:
        upd_ship = update_spaceship_status(id, new_status)
    except ValueError as err:
        return {'error': str(err)}, 400
    
    result = SpaceshipSchema().dump(upd_ship)
    return jsonify(result), 200


@app.delete('/api/v1/spaceships/<id>')
def delete_ship_controller(id):
    try:
        delete_spaceship(id)
    except ValueError as err:
        return {'error': str(err)}, 400
    
    return 'Successful deletion', 200
    



def run_server():
    app.run(port=5000, debug=True)

run_server()

