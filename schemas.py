from marshmallow import Schema, fields 


class ItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True)

class ItemGetSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    price = fields.Int(dump_only=True)


class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only=True)

class ItemQuerySchema(Schema):
    id = fields.Str(required=True)

class ItemOptionalQuerySchema(Schema):
    id = fields.Str(required=False)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserQuerySchema(Schema):
    id = fields.Int(required=True)