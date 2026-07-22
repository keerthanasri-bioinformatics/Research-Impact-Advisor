from flask import Blueprint, render_template, request, redirect, url_for

from models.project import db
from models.pipeline import Pipeline
from models.tool import Tool

tool_bp = Blueprint("tool", __name__)


@tool_bp.route("/tools")
def tools():

    all_tools = Tool.query.all()

    return render_template(
        "tools.html",
        tools=all_tools
    )


@tool_bp.route("/tools/new", methods=["GET", "POST"])
def new_tool():

    pipelines = Pipeline.query.all()

    if request.method == "POST":

        tool = Tool(

            pipeline_id=request.form["pipeline_id"],
            tool_name=request.form["tool_name"],
            version=request.form["version"],
            purpose=request.form["purpose"]

        )

        db.session.add(tool)
        db.session.commit()

        return redirect(url_for("tool.tools"))

    return render_template(
        "create_tool.html",
        pipelines=pipelines
    )


@tool_bp.route("/tools/delete/<int:id>")
def delete_tool(id):

    tool = Tool.query.get_or_404(id)

    db.session.delete(tool)
    db.session.commit()

    return redirect(url_for("tool.tools"))