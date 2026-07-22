from flask import Blueprint, render_template, redirect, url_for

from models.project import db
from models.analysis import Analysis

analysis_bp = Blueprint("analysis", __name__)


@analysis_bp.route("/analysis")
def analysis_history():

    analyses = Analysis.query.order_by(
        Analysis.id.desc()
    ).all()

    return render_template(
        "analysis_history.html",
        analyses=analyses
    )


@analysis_bp.route("/analysis/<int:id>")
def analysis_details(id):

    analysis = Analysis.query.get_or_404(id)

    return render_template(
        "analysis_details.html",
        analysis=analysis
    )


@analysis_bp.route("/analysis/delete/<int:id>")
def delete_analysis(id):

    analysis = Analysis.query.get_or_404(id)

    db.session.delete(analysis)
    db.session.commit()

    return redirect(
        url_for("analysis.analysis_history")
    )