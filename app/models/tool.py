from models.project import db

class Tool(db.Model):

    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)

    pipeline_id = db.Column(
        db.Integer,
        db.ForeignKey("pipelines.id"),
        nullable=False
    )

    tool_name = db.Column(
        db.String(100),
        nullable=False
    )

    version = db.Column(
        db.String(50),
        nullable=False
    )

    purpose = db.Column(
        db.String(200)
    )

    pipeline = db.relationship(
        "Pipeline",
        backref="tools"
    )