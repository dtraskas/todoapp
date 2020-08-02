
import jsonschema
import logging

from http import HTTPStatus
from flask import request, jsonify, url_for
from flask_restx import Namespace, Resource, fields, abort, reqparse

from .models import (
    make_request_model
)

from ..restplus import API

def register_namespace():
    
    namespace = API.namespace('tasks', description='Resource managing tasks.')
    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web', 
            'done': False
        }
    ]
    
    @namespace.route('/')
    class TaskEntity(Resource):
        
        def __init__(self, api=None, *args, **kwargs):
            super().__init__(api, args, kwargs)
            self._logger = logging.getLogger(__name__)            

        @API.doc('create_task')
        @API.expect(make_request_model(), validate=True)
        def post(self):
            if not request.json or not 'title' in request.json:
                abort(400)
            task = {
                'id': tasks[-1]['id'] + 1,
                'title': request.json['title'],
                'description': request.json.get('description', ""),
                'done': False
            }
            tasks.append(task)
            return 201

        @API.doc('get_tasks')
        def get(self):
            return jsonify( { 'tasks': tasks } )

    return namespace