from flask import Blueprint

api_bp = Blueprint("api", __name__)


@api_bp.route("/", methods=["GET"])
def home():
    return {
        "application": "DeployForge",
        "message": "Welcome to DeployForge",
        "status": "running"
    }

@api_bp.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}, 200
