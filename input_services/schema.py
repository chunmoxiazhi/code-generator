from marshmallow import Schema, fields

class ParameterSchema(Schema):
    key = fields.Str()
    value = fields.Str(required=False)

class EndpointSchema(Schema):
    request_method = fields.Str(validate=lambda x: x in ["POST", "PUT", "GET", "DELETE", "PATCH"])
    url = fields.Str()
    query_parameters = fields.Nested(ParameterSchema, many=True, required=False)
    path_parameters = fields.List(fields.Str(), required=False)
    request_body = fields.Field(required=False)
    headers = fields.Raw()
    name = fields.Str()