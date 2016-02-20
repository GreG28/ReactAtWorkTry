#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.restful import  reqparse, abort, Api, Resource
from flask.ext.cors import CORS
from flask_restful_swagger import swagger
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__, static_url_path='')
CORS(app)

###################################
# Wrap the Api with swagger.docs. It is a thin wrapper around the Api class that adds some swagger smarts
api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/api/spec', produces=["application/json", "text/html"],  description='API Pour fournir des données à React')
###################################


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

TASKS = {
    'task1': {'task': 'build an API'},
    'task2': {'task': '?????'},
    'task3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message="Task {} doesn't exist".format(task_id))

parser = reqparse.RequestParser()
parser.add_argument('task')
# From the request headers
parser.add_argument('User-Agent', location='headers')

@swagger.model
class TodoItemWithArgs:
    def __init__(self, arg1, arg2, arg3='123'):
        pass


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    @swagger.operation(notes='just testing inheritance',
      nickname='getTodoSpecific')
    def get(self, todo_id):
        args = parser.parse_args()
        print(args)
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    @swagger.operation(notes='Delete TODO',
        responseClass=TodoItemWithArgs.__name__,
        nickname='delete',
        parameters=[
            {
              "name": "body",
              "description": "blueprint object that needs to be added. JSON.",
              "required": True,
              "allowMultiple": False,
              "dataType": str.__name__,
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 201,
              "message": "Created. The URL of the created blueprint should be in the Location header"
            },
            {
              "code": 405,
              "message": "Invalid input"
            }
          ]
        )
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    @swagger.operation()
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    @swagger.operation(notes='just testing inheritance',
      nickname='getTodos')
    def get(self):
        return TODOS

    @swagger.operation(notes='POST TODOS',
      nickname='postTodos')
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# Todo
# shows a single todo item and lets you delete a todo item
class Task(Resource):

    @swagger.operation()
    def get(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        return TASKS[task_id]

    @swagger.operation()
    def delete(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        del TASKS[task_id]
        return '', 204

    @swagger.operation()
    def put(self, task_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TASKS[task_id] = task
        return task, 201



COMMENTS = [
  {"id" : 1, "author": "Pete Hunt", "text": "This is one comment"},
  {"id" : 2, "author": "Jordan Walke", "text": "This is *another* comment"},
  {"id" : 5, "author": "GF 1", "text": "This is one comment"},
  {"id" : 6, "author": "GF 3", "text": "* This is one comment"}
]


# Comments
# shows a single todo item and lets you delete a todo item
class Comments(Resource):

    @swagger.operation()
    def get(self):
        return COMMENTS

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/api/todos', endpoint="All TODOS")
api.add_resource(Todo, '/api/todos/<todo_id>', endpoint="TODOS specific id")
api.add_resource(Task, '/api/tasks/<task_id>', endpoint="TASK")

# Ajout des commentaires à l'API
api.add_resource(Comments, '/api/comments', endpoint="COMMENTS")

@app.route('/docs')
def docs():
    return redirect('/static/docs.html')

@app.route('/')
def root():
    print(' Local file ? ')
    return app.send_static_file('../index.html')

if __name__ == '__main__':
    handler = RotatingFileHandler('output.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=8090, debug=True)
