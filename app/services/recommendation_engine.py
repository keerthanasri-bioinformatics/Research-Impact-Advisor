def generate_recommendation(impact_results):

    high = 0
    medium = 0
    low = 0

    reasons = []

    for item in impact_results:

        if item["priority"] == "High":
            high += 1
            reasons.append(
                f'{item["tool_name"]} has a HIGH impact update.'
            )

        elif item["priority"] == "Medium":
            medium += 1
            reasons.append(
                f'{item["tool_name"]} has a MEDIUM impact update.'
            )

        elif item["priority"] == "Low":
            low += 1

    if high > 0:

        recommendation = "Reanalysis Recommended"

        priority = "HIGH"

    elif medium > 0:

        recommendation = "Review Before Reanalysis"

        priority = "MEDIUM"

    else:

        recommendation = "No Reanalysis Needed"

        priority = "LOW"

    return {

        "recommendation": recommendation,

        "priority": priority,

        "reasons": reasons

    }