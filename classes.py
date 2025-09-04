from typing import List
from dataclasses import dataclass

@dataclass
class Ship:
    spaceship_id: str
    name: str
    type_: str
    status: str  # 'available', 'on mission', 'under repair'

    def __init__(self, spaceship_id: str, name: str, type_: str, status: str = 'available'):
        self.spaceship_id = spaceship_id
        self.name = name
        self.type_ = type_
        self.status = status

    def update_status(self, new_status: str):
        self.status = new_status

#    def __repr__(self):
#        return f'spaceship {self.spaceship_id}:\n\tname: {self.name};\n\ttype: {self.type_};\n\tstatus: {self.status}'

@dataclass
class Mission:
    mission_id: str
    name: str
    goal: str  # 'exploration', 'defence'
    status: str  # 'planned', 'in process', 'completed'
    spaceships: List[str] # list of spaceship_id's

    def __init__(self, mission_id: str, name: str, goal: str, status: str = 'planned', spaceships: List[str] = []):
        self.mission_id = mission_id
        self.name = name
        self.goal = goal
        self.status = status
        self.spaceships = spaceships

    def add_spaceship(self, spaceship: str):
        self.spaceships.append(spaceship)

#    def __repr__(self):
#        return f'mission {self.mission_id}:\n\tname: {self.name};\n\tgoal: {self.goal};\n\t status: {self.status};\n\t spaceships: {self.spaceships}'

@dataclass
class CrewMember:
    member_id: str
    name: str
    role: str  # 'captain', 'engineer', 'pilot'

    def __init__(self, member_id: str, name: str, role: str):
        self.member_id = member_id
        self.name = name
        self.role = role

#    def __repr__(self):
#        return f'crew member {self.member_id}:\n\tname: {self.name};\n\trole: {self.role}'
