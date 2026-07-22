from models.tool import Tool
from models.reference_database import ReferenceDatabase
from models.latest_version import LatestVersion


def analyze_pipeline(pipeline_id):

    results = []

    # Compare tools
    tools = Tool.query.filter_by(pipeline_id=pipeline_id).all()

    for tool in tools:

        latest = LatestVersion.query.filter_by(
            software_name=tool.tool_name,
            category="Tool"
        ).first()

        if latest:

            if tool.version == latest.latest_version:
                status = "Up-to-date"
            else:
                status = "Outdated"

            results.append({

                "type": "Tool",
                "name": tool.tool_name,
                "current": tool.version,
                "latest": latest.latest_version,
                "status": status

            })

    # Compare databases
    databases = ReferenceDatabase.query.filter_by(
        pipeline_id=pipeline_id
    ).all()

    for database in databases:

        latest = LatestVersion.query.filter_by(
            software_name=database.database_name,
            category="Database"
        ).first()

        if latest:

            if database.version == latest.latest_version:
                status = "Up-to-date"
            else:
                status = "Outdated"

            results.append({

                "type": "Database",
                "name": database.database_name,
                "current": database.version,
                "latest": latest.latest_version,
                "status": status

            })

    return results