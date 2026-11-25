from flask import Blueprint, render_template
from ..db import ping_db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/api/health")
def health():
    try:
        ping_db()
        return {"status": "ok", "app": "GradBridge", "database": "connected"}
    except Exception as exc:
        return {"status": "error", "database": str(exc)}, 500