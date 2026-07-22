from flask import Blueprint, render_template, request, redirect, url_for

from models.project import db
from models.latest_version import LatestVersion

latest_bp = Blueprint("latest", __name__)


@latest_bp.route("/latest_versions")
def latest_versions():

    versions = LatestVersion.query.all()

    return render_template(
        "latest_versions.html",
        versions=versions
    )


@latest_bp.route("/latest_versions/new", methods=["GET", "POST"])
def new_latest_version():

    if request.method == "POST":

        version = LatestVersion(

            software_name=request.form["software_name"],
            category=request.form["category"],
            latest_version=request.form["latest_version"],
            release_date=request.form["release_date"],
            source=request.form["source"]

        )

        db.session.add(version)
        db.session.commit()

        return redirect(url_for("latest.latest_versions"))

    return render_template("create_latest_version.html")


@latest_bp.route("/latest_versions/delete/<int:id>")
def delete_latest_version(id):

    version = LatestVersion.query.get_or_404(id)

    db.session.delete(version)

    db.session.commit()

    return redirect(url_for("latest.latest_versions"))