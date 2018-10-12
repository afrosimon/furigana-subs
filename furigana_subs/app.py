from flask import Flask
from .views import index_page


def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = '/tmp'
    app.register_blueprint(index_page)

    return app
