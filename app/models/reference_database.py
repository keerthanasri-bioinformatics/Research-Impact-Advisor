from models.project import db

class ReferenceDatabase(db.Model):

    __tablename__ = "reference_databases"

    id = db.Column(db.Integer, primary_key=True)

    pipeline_id = db.Column(
        db.Integer,
        db.ForeignKey("pipelines.id"),
        nullable=False
    )

    database_name = db.Column(
        db.String(100),
        nullable=False
    )

    version = db.Column(
        db.String(50),
        nullable=False
    )

    release_date = db.Column(
        db.String(50)
    )

    pipeline = db.relationship(
        "Pipeline",
        backref="reference_databases"
    )