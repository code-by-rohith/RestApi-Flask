from marshmallow import Schema , fields 


class DataValidation(Schema):
    name = fields.String(required= True)
    roll_no= fields.Int(required= True)

user_schema = DataValidation()
user_list_schema = DataValidation(many=True)
