from flask import Blueprint, send_file
import os

from models.analysis import Analysis
from reports.report_generator import generate_report

report_bp = Blueprint("report", __name__)


@report_bp.route("/report/<int:id>")
def report(id):

    analysis = Analysis.query.get_or_404(id)

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/analysis_{id}.pdf"

    generate_report(
        analysis,
        filename
    )

    return send_file(
        filename,
        as_attachment=True
    )