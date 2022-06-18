from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Spot, Image

spot_routes = Blueprint('spots', __name__)

@spot_routes.route('/')
@login_required
def spots():
    spots = Spot.query.all()
    return jsonify([spot.to_dict() for spot in spots])
