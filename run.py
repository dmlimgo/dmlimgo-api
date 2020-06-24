from flask import Flask
from flask_restplus import Api, Resource

from route import etc_route

app = Flask(__name__)
app.debug = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'
api = Api(app, 
          version='1.0',
          title='Api Server',
          description='A simple Api',
          doc='/swagger')


def add_namespace():
    api.add_namespace(etc_route.api)

add_namespace()

if __name__ == '__main__':
    app.run()