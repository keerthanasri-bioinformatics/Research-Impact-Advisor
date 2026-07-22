from flask import Blueprint, render_template, request, redirect, url_for

from models.project import db
from models.pipeline import Pipeline
from models.reference_database import ReferenceDatabase

database_bp = Blueprint("database", __name__)


@database_bp.route("/databases")
def databases():

    all_databases = ReferenceDatabase.query.all()

    return render_template(
        "databases.html",
        databases=all_databases
    )


@database_bp.route("/databases/new", methods=["GET", "POST"])
def new_database():

    pipelines = Pipeline.query.all()

    if request.method == "POST":

        database = ReferenceDatabase(

            pipeline_id=request.form["pipeline_id"],
            database_name=request.form["database_name"],
            version=request.form["version"],
            release_date=request.form["release_date"]

        )

        db.session.add(database)
        db.session.commit()

        return redirect(url_for("database.databases"))

    return render_template(
        "create_database.html",
        pipelines=pipelines
    )


@database_bp.route("/databases/delete/<int:id>")
def delete_database(id):

    database = ReferenceDatabase.query.get_or_404(id)

    db.session.delete(database)
    db.session.commit()

    return redirect(url_for("database.databases"))