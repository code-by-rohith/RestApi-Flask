from marshmallow import fields, Schema, post_load

class StudentData(Schema):
    ids = fields.Int(required=True)
    name = fields.Str(required=True)
    roll_no = fields.Str(required=True)
    Mark_1 = fields.Int(required=True)
    Mark_2 = fields.Int(required=True)
    Total = fields.Int(required=False)  

    @post_load
    def compute_total(self, data,**kwargs):
        data['Total'] = data['Mark_1'] + data['Mark_2']  
        return data

obj = StudentData()
obj_many = StudentData(many=True)
