from marshmallow import Schema, fields

class SpaceshipSchema(Schema):
    name = fields.Str(required=True)
    type_ = fields.Str(required=True)
    status = fields.Str(required=False, dump_default="available")

class SpaceshipUpdateSchema(Schema):
    status = fields.Str(required=True)


