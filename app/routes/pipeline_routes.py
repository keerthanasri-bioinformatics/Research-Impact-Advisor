from flask import Blueprint, render_template, request, redirect, url_for

from models.project import db
from models.project import Project
from models.pipeline import Pipeline

pipeline_bp = Blueprint("pipeline", __name__)


@pipeline_bp.route("/pipelines")
def pipelines():

    pipelines = Pipeline.query.all()

    return render_template(
        "pipelines.html",
        pipelines=pipelines
    )


@pipeline_bp.route("/pipelines/new", methods=["GET", "POST"])
def new_pipeline():

    projects = Project.query.all()

    if request.method == "POST":

        pipeline = Pipeline(

            project_id=request.form["project_id"],
            pipeline_name=request.form["pipeline_name"],
            version=request.form["version"],
            description=request.form["description"]

        )

        db.session.add(pipeline)
        db.session.commit()

        return redirect(url_for("pipeline.pipelines"))

    return render_template(
        "create_pipeline.html",
        projects=projects
    )


@pipeline_bp.route("/pipelines/delete/<int:id>")
def delete_pipeline(id):

    pipeline = Pipeline.query.get_or_404(id)

    db.session.delete(pipeline)
    db.session.commit()

    return redirect(url_for("pipeline.pipelines"))