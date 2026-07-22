from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(analysis, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>Research Impact Advisor Report</b>",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "<br/>",
            styles["Normal"]
        )
    )

    data = [

        ["Project",
         analysis.project.project_name],

        ["Pipeline",
         analysis.pipeline.pipeline_name],

        ["Analysis Date",
         analysis.analysis_date],

        ["Updates Found",
         str(analysis.updates_found)],

        ["High Impact",
         str(analysis.high_impact)],

        ["Medium Impact",
         str(analysis.medium_impact)],

        ["Low Impact",
         str(analysis.low_impact)],

        ["Priority",
         analysis.priority],

        ["Recommendation",
         analysis.recommendation]

    ]

    table = Table(
        data,
        colWidths=[150,300]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("BACKGROUND",(0,0),(-1,0),colors.grey)

        ])

    )

    elements.append(table)

    doc.build(elements)