from models.project import db


class Pipeline(db.Model):

    __tablename__ = "pipelines"

    id = db.Column(db.Integer, primary_key=True)

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False
    )

    pipeline_name = db.Column(
        db.String(200),
        nullable=False
    )

    version = db.Column(
        db.String(100)
    )

    description = db.Column(
        db.Text
    )

    project = db.relationship(
        "Project",
        backref="pipelines"
    )