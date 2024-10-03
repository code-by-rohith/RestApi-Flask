from marshmallow import fields, Schema, validate

class DetailedData(Schema):
    roll_no = fields.Int(required=True)
    name = fields.Str(required=True)
    total = fields.Float(required=True)

detailed_data = DetailedData()
detailed_data_multiple = DetailedData(many=True)

class TendanceAlort(Schema):
    ticketno = fields.Int(required=True)
    train_name = fields.Str(required=True)
    destination = fields.Str(required=True)
    shift = fields.Str(required=True, validate=validate.OneOf(["Morning", "Afternoon", "Night"]))

obj_tendancy_alort_single = TendanceAlort()
obj_tendancy_alort_multiple = TendanceAlort(many=True)
