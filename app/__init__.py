# third-party imports
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from app.config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    from app import models

    migrate = Migrate(app, db)


    # temporary route
    @app.route('/', methods=['GET'])
    def hello_world():
        # GET
        bets = models.Bet.get_all()
        results = []

        for bet in bets:
            obj = {
                'id': bet.id,
                'max_users': bet.max_users,
                'title': bet.title,
                'text': bet.text,
                'amount': bet.amount,
                'completed': bet.completed
            }
            results.append(obj)

        response = jsonify(results)
        response.status_code = 200
        return response

    return app