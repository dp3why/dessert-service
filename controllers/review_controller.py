import os
from services.connect import *
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from dotenv import load_dotenv

load_dotenv()

review_blueprint = Blueprint('reviews', __name__)

MONGODB_CONNECTION_STRING = os.getenv("MONGO_URI")
MONGODB_DATABASE = 'ch'

# POST create a user


@review_blueprint.route('/reviews', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def create_user():

    data = request.get_json()
    client, collection = connect_mongo('users')

    newReview = {}
    newReview['_id'] = data['uid']
    newReview['name'] = data['name']
    newReview['email'] = data['email']
    newReview['photoURL'] = data['photoURL']

    collection.insert_one(newReview)
    client.close()

    return jsonify(newReview), 201
