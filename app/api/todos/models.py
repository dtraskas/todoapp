"""
Provides request and response serializers for RESTful resources
"""
from flask_restx import fields, reqparse
from ..restplus import API

def make_request_model():
    model_name = 'TodoRequest'
    if model_name not in API.models:
        _fields = {
            'title': fields.String(
                required=True,
                description="Title for TODO item",
                example='Buy groceries'
            ),
            'description': fields.String(
                required=True,
                description="Full description of the TODO item",
                example='Buy shampoo, cereal and fruit'
            ),
            'done': fields.Boolean(
                required=True,
                description="Flags the TODO item as done or not",
                example=False
            )
        }
        API.model(model_name, _fields)
    return API.models[model_name]