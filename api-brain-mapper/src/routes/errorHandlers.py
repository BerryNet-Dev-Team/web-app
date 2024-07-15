from flask import Blueprint, jsonify

errorHandlers = Blueprint('error_handlers', __name__)

@errorHandlers.app_errorhandler(400)
def handle400(e):
    return jsonify(error=str(e)), 400

@errorHandlers.app_errorhandler(401)
def handle401(e):
    return jsonify(error=str(e)), 401

@errorHandlers.app_errorhandler(403)
def handle403(e):
    return jsonify(error=str(e)), 403

@errorHandlers.app_errorhandler(404)
def handle404(e):
    return jsonify(error=str(e)), 404

@errorHandlers.app_errorhandler(500)
def handle500(e):
    return jsonify(error=str(e)), 500