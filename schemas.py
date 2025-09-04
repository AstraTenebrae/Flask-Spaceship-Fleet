from marshmallow import Schema, fields

class SpaceshipSchema(Schema):
    name = fields.Str(required=True)
    type_ = fields.Str(required=True)
    status = fields.Str(required=False, dump_default="available")

class SpaceshipUpdateSchema(Schema):
    status = fields.Str(required=True)

class MissionSchema(Schema):
    name = fields.Str(required=True)
    goal = fields.Str(required=True)
    status = fields.Str(required=False, dump_default="planned")

class MissionAddShipSchema(Schema):
    spaceship_id = fields.Str(required=True)
