from models.project import db


class Analysis(db.Model):

    __tablename__ = "analysis"

    id = db.Column(db.Integer, primary_key=True)

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False
    )

    pipeline_id = db.Column(
        db.Integer,
        db.ForeignKey("pipelines.id"),
        nullable=False
    )

    analysis_date = db.Column(db.String(50))

    updates_found = db.Column(db.Integer)

    high_impact = db.Column(db.Integer)

    medium_impact = db.Column(db.Integer)

    low_impact = db.Column(db.Integer)

    recommendation = db.Column(db.String(200))

    priority = db.Column(db.String(20))

    project = db.relationship(
        "Project",
        backref="analyses"
    )

    pipeline = db.relationship(
        "Pipeline",
        backref="analyses"
    )