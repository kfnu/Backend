from flask import request, jsonify, abort, Blueprint


from app import models

betRoutes = Blueprint('betsBp', __name__)

@betRoutes.route('/', methods=['GET'])
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