from flask import Blueprint, render_template, request
from datetime import datetime

from models.project import db
from models.pipeline import Pipeline
from models.analysis import Analysis

from services.update_checker import analyze_pipeline
from services.impact_engine import calculate_impact

update_bp = Blueprint("update", __name__)


@update_bp.route("/updates")
def updates():

    pipelines = Pipeline.query.all()

    return render_template(
        "update_checker.html",
        pipelines=pipelines
    )


@update_bp.route("/updates/analyze", methods=["POST"])
def analyze():

    pipeline_id = int(request.form["pipeline_id"])

    pipeline = Pipeline.query.get_or_404(pipeline_id)

    results = analyze_pipeline(pipeline_id)

    impact = calculate_impact(results)

    updates_found = (
        impact["high"] +
        impact["medium"] +
        impact["low"]
    )

    analysis = Analysis(

        project_id=pipeline.project_id,

        pipeline_id=pipeline.id,

        analysis_date=datetime.now().strftime("%d-%m-%Y"),

        updates_found=updates_found,

        high_impact=impact["high"],

        medium_impact=impact["medium"],

        low_impact=impact["low"],

        recommendation=", ".join(
            impact["recommendations"]
        ),

        priority=impact["priority"]

    )

    db.session.add(analysis)

    db.session.commit()

    pipelines = Pipeline.query.all()

    return render_template(

        "update_checker.html",

        pipelines=pipelines,

        results=results,

        impact=impact

    )