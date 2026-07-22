from services.update_checker import compare_versions

project_tools = [

    {
        "tool_name": "FastQC",
        "version": "0.11.9"
    },

    {
        "tool_name": "BWA",
        "version": "0.8.0"
    },

    {
        "tool_name": "SAMtools",
        "version": "1.18"
    }

]

latest_versions = {

    "FastQC": "0.12.0",

    "BWA": "0.8.0",

    "SAMtools": "1.20"

}

results = compare_versions(project_tools, latest_versions)

for result in results:

    print("-----------------------------")

    print("Tool:", result["tool_name"])

    print("Current Version:", result["current_version"])

    print("Latest Version:", result["latest_version"])

    print("Status:", result["status"])