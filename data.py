from typing import List
from classes import Ship, Mission, CrewMember
from marshmallow import Schema, ValidationError
from flask import request
import uuid

spaceships: List[Ship] = [Ship('1', 'ship_1', 'type 1'), Ship('2', 'ship_2', 'type 1')]
missions: List[Mission] = []

supported_spaceship_statuses = ('available', 'on mission', 'under repair')
supported_mission_goals = ('exploration', 'defence')
supported_mission_statuses = ('planned', 'in progress', 'completed')
supported_crewmember_roles = ('captain', 'engineer', 'pilot')

def check_status(new_status: str):
    if new_status not in supported_spaceship_statuses:
        raise ValueError(f'Unsupported spaceship status: {new_status}')
    
def check_goal(goal: str):
    if goal not in supported_mission_goals:
        raise ValueError(f'Unsupported mission goal: {goal}')
    
def check_mission_status(mission_status: str):
    if mission_status not in supported_mission_statuses:
        raise ValueError(f'Unsupported mission status: {mission_status}')



def get_spaceships_list():
    return spaceships

def get_spaceship_by_id(id: str):
    return next((i for i in spaceships if i.spaceship_id == id), None)

def get_mission_by_id(id: str):
    return next((i for i in missions if i.mission_id == id), None)




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

def add_mission(name_arg: str, goal_arg: str, status_arg: str = 'planned'):
    check_mission_status(status_arg)
    check_goal(goal_arg)
    mission = Mission(
        mission_id = str(uuid.uuid4()),
        name = name_arg,
        goal = goal_arg,
        status = status_arg,
        spaceships = []
    )
    missions.append(mission)
    return mission




def update_spaceship_status(id: str, new_status: str):
    check_status(new_status)
    
    spaceship = get_spaceship_by_id(id)
    if spaceship is None:
        raise ValueError('Spaceship not found')
    if new_status == 'available':
        for mission in missions:
            if id in mission.spaceships:
                mission.spaceships.remove(id)
    
    spaceship.update_status(new_status)
    return spaceship

def add_ship_to_mission(mission_id: str, spaceship_id: str):
    mission = get_mission_by_id(mission_id)
    spaceship = get_spaceship_by_id(spaceship_id)
    if mission is None:
        raise ValueError('Mission not found')
    if spaceship is None:
        raise ValueError('Spaceship not found')
    if spaceship.status != 'available':
        raise ValueError('Spaceship is not available')

    mission.add_spaceship(spaceship_id)
    spaceship.update_status('on mission')
    return mission


def delete_spaceship(id: str):
    global spaceships
    spaceship = get_spaceship_by_id(id)
    if spaceship is None:
        raise ValueError('Spaceship not found')
    for mission in missions:
        if id in mission.spaceships:
            mission.spaceships.remove(id)
    spaceships = [ship for ship in spaceships if ship.spaceship_id != id]


def get_missions_list():
    return missions