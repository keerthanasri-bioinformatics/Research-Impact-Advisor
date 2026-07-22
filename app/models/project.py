from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)

    project_name = db.Column(db.String(200), nullable=False)

    researcher = db.Column(db.String(200))

    organization = db.Column(db.String(200))

    project_type = db.Column(db.String(200))

    organism = db.Column(db.String(200))

    description = db.Column(db.Text)

    status = db.Column(db.String(50), default="Active")