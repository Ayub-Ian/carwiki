from marshmallow import Schema, fields

class ItemUpdateSchema(Schema):
    make = fields.Str(required=False)
    model = fields.Str(required=False)
    year = fields.Int(required=False)
    color = fields.Str(required=False)
    mileage = fields.Int(required=False)
    imageUrl = fields.Str(required=False, attribute='image_url')
