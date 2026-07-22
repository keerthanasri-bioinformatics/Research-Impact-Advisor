from flask import Flask, render_template

# Database
from models.project import db
from models.project import Project
from models.pipeline import Pipeline
from models.tool import Tool
from models.reference_database import ReferenceDatabase
from models.latest_version import LatestVersion
from models.analysis import Analysis

# Routes
from routes.project_routes import project_bp
from routes.pipeline_routes import pipeline_bp
from routes.tool_routes import tool_bp
from routes.database_routes import database_bp
from routes.latest_version_routes import latest_bp
from routes.update_checker_routes import update_bp
from routes.analysis_routes import analysis_bp
from routes.report_routes import report_bp

app = Flask(__name__)

# NEW DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///research_v2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(project_bp)
app.register_blueprint(pipeline_bp)
app.register_blueprint(tool_bp)
app.register_blueprint(database_bp)
app.register_blueprint(latest_bp)
app.register_blueprint(update_bp)
app.register_blueprint(analysis_bp)
app.register_blueprint(report_bp)


@app.route("/")
def dashboard():

    stats = {
        "projects": Project.query.count(),
        "pipelines": Pipeline.query.count(),
        "tools": Tool.query.count(),
        "databases": ReferenceDatabase.query.count(),
        "versions": LatestVersion.query.count(),
        "analyses": Analysis.query.count()
    }

    recent_projects = Project.query.order_by(
        Project.id.desc()
    ).limit(5).all()

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_projects=recent_projects
    )


if __name__ == "__main__":
    app.run(debug=True)