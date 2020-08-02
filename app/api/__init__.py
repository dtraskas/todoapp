from .restplus import API, register_swagger
from .todos.resource import register_namespace as register_todos
from .default.resource import register_namespace as register_default