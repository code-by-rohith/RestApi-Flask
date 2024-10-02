from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    name = fields.String(required=True)
    rollno = fields.Integer(required=True)
    total_marks = fields.Float(required=True)
    grade = fields.String(required=True, validate=validate.OneOf(["A", "B", "C"]))

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)  
