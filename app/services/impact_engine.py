def calculate_impact(results):

    high = 0
    medium = 0
    low = 0

    recommendations = []

    for item in results:

        if item["status"] != "Outdated":
            continue

        # ---------- TOOLS ----------

        if item["type"] == "Tool":

            if item["name"] == "BWA":
                high += 1
                recommendations.append(
                    "Re-align sequencing reads using the latest BWA version."
                )

            elif item["name"] == "FastQC":
                medium += 1
                recommendations.append(
                    "Re-run Quality Control using the latest FastQC."
                )

            elif item["name"] == "SAMtools":
                medium += 1
                recommendations.append(
                    "Validate BAM processing using the latest SAMtools."
                )

            else:
                low += 1
                recommendations.append(
                    f"Review updates for {item['name']}."
                )

        # ---------- DATABASES ----------

        elif item["type"] == "Database":

            if item["name"] == "ClinVar":
                high += 1
                recommendations.append(
                    "Re-annotate variants using the latest ClinVar release."
                )

            elif item["name"] == "Ensembl":
                medium += 1
                recommendations.append(
                    "Review gene annotations using the latest Ensembl release."
                )

            elif item["name"] == "dbSNP":
                medium += 1
                recommendations.append(
                    "Re-run variant annotation with the latest dbSNP."
                )

            else:
                low += 1
                recommendations.append(
                    f"Review updates for {item['name']}."
                )

    if high > 0:
        priority = "HIGH"
    elif medium > 0:
        priority = "MEDIUM"
    elif low > 0:
        priority = "LOW"
    else:
        priority = "NONE"

    return {
        "high": high,
        "medium": medium,
        "low": low,
        "priority": priority,
        "recommendations": recommendations
    }