from models.project import db

class LatestVersion(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    software_name = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    latest_version = db.Column(db.String(50), nullable=False)

    release_date = db.Column(db.String(50))

    source = db.Column(db.String(200))