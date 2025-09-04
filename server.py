from flask import Flask, request, jsonify
from data import add_spaceship, add_mission, get_spaceships_list, get_spaceship_by_id, update_spaceship_status, add_ship_to_mission, check_status, check_mission_status, check_goal, delete_spaceship, get_missions_list
from schemas import SpaceshipSchema, SpaceshipUpdateSchema, MissionSchema, MissionAddShipSchema
from marshmallow import ValidationError

app = Flask(__name__)


def check_request(schema_class):
    if request.json is None:
        return dict(), {"error": "No JSON provided"}, 400
    schema = schema_class()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return dict(), {"error": err.messages}, 400    
    if not data or not isinstance(data, dict):
        return dict(), {"error": "Wrong data format"}, 400
    return data, None, 0



@app.get('/api/v1/spaceships')
def get_spaceships_list_controller():
    return get_spaceships_list(), 200


@app.get('/api/v1/missions')
def get_missions_list_controller():
    return get_missions_list(), 200


@app.get('/api/v1/spaceships/<id>')
def get_spaceship_by_id_controller(id: str):
    spaceship = get_spaceship_by_id(id)
    if spaceship is None:
        return {"error": "Spaceship not found"}, 404
    return jsonify(spaceship), 200


@app.post('/api/v1/spaceships')
def create_spaceship_controller():
    data, error, code = check_request(SpaceshipSchema)
    if error:
        return error, code
    
    try:
        new_ship = add_spaceship(data['name'], data['type_'], data.get('status', 'available'))
    except ValueError as err:
        return {"error": str(err)}, 400
    result = SpaceshipSchema().dump(new_ship)
    return jsonify(result), 201


@app.post('/api/v1/missions')
def create_mission_controller():
    data, error, code = check_request(MissionSchema)
    if error:
        return error, code
    try:
        new_mission = add_mission(data['name'], data['goal'], data.get('status', 'planned'))
    except ValueError as err:
        return {'error': str(err)}, 400
    result = MissionSchema().dump(new_mission)
    return jsonify(result), 201



@app.patch('/api/v1/spaceships/<id>')
def update_status_controller(id: str):
    data, error, code = check_request(SpaceshipUpdateSchema)
    if error:
        return error, code
    try:
        upd_ship = update_spaceship_status(id, data['status'])
    except ValueError as err:
        return {'error': str(err)}, 400
    result = SpaceshipSchema().dump(upd_ship)
    return jsonify(result), 200


@app.patch('/api/v1/missions/<id>')
def add_ship_to_mission_controller(id: str):
    data, error, code = check_request(MissionAddShipSchema)
    if error:
        return error, code
    
    try:
        upd_mission = add_ship_to_mission(id, data['spaceship_id'])
    except ValueError as err:
        return {'error': str(err)}, 400
    result = MissionSchema().dump(upd_mission)
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

