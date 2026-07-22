from flask import Blueprint, render_template, request, redirect, url_for

from models.project import Project, db

project_bp = Blueprint("project", __name__)


@project_bp.route("/projects")
def projects():

    all_projects = Project.query.all()

    return render_template(
        "projects.html",
        projects=all_projects
    )


@project_bp.route("/projects/new", methods=["GET", "POST"])
def new_project():

    if request.method == "POST":

        project = Project(

            project_name=request.form["project_name"],
            researcher=request.form["researcher"],
            organization=request.form["organization"],
            project_type=request.form["project_type"],
            organism=request.form["organism"],
            description=request.form["description"]

        )

        db.session.add(project)
        db.session.commit()

        return redirect(url_for("project.projects"))

    return render_template("create_project.html")


@project_bp.route("/projects/delete/<int:id>")
def delete_project(id):

    project = Project.query.get_or_404(id)

    db.session.delete(project)

    db.session.commit()

    return redirect(url_for("project.projects"))