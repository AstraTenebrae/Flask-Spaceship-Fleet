from typing import List
from classes import Ship, Mission, CrewMember
import uuid

spaceships: List[Ship] = [Ship('1', 'ship_1', 'type 1'), Ship('2', 'ship_2', 'type 1')]
missions: List[Mission] = []

def check_status(new_status: str):
    if new_status not in ('available', 'on mission', 'under repair'):
        raise ValueError(f'Unsupported spaceship status: {new_status}')

def get_spaceships_list():
    return spaceships

def get_spaceship_by_id(id: str):
    return next((i for i in spaceships if i.spaceship_id == id), None)

def add_spaceship(name_arg: str, type_arg: str, status_arg: str = 'available'):
    check_status(status_arg)
    ship = Ship(
        spaceship_id = str(uuid.uuid4()),
        name = name_arg,
        type_ = type_arg,
        status = status_arg
    )
    spaceships.append(ship)

    return ship

def update_spaceship_status(id: str, new_status: str):
    check_status(new_status)
    
    spaceship = get_spaceship_by_id(id)
    if spaceship is None:
        raise ValueError('Spaceship not found')
    
    check_status(new_status)
    
    spaceship.update_status(new_status)
    return spaceship

def delete_spaceship(id: str):
    global spaceships
    spaceship = get_spaceship_by_id(id)
    if spaceship is None:
        raise ValueError('Spaceship not found')
    spaceships = [ship for ship in spaceships if ship.spaceship_id != id]