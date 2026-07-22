from app import app
from models.project import db
from models.latest_version import LatestVersion

with app.app_context():

    db.session.query(LatestVersion).delete()

    data = [

        LatestVersion(
            software_name="FastQC",
            category="Tool",
            latest_version="0.12.0",
            release_date="2024-03-15",
            source="GitHub"
        ),

        LatestVersion(
            software_name="BWA",
            category="Tool",
            latest_version="0.8.0",
            release_date="2024-05-10",
            source="GitHub"
        ),

        LatestVersion(
            software_name="SAMtools",
            category="Tool",
            latest_version="1.20",
            release_date="2024-06-01",
            source="GitHub"
        )

    ]

    db.session.add_all(data)

    db.session.commit()

    print("Latest versions added successfully!")