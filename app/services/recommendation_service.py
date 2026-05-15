def generate_recommendation(

    temperature,
    vibration,
    voltage,
    pressure,
    runtime_hours,
):

    recommendations = []

    if temperature > 85:

        recommendations.append(
            "High temperature detected. Inspect cooling system."
        )

    if vibration > 4:

        recommendations.append(
            "Excessive vibration detected. Check mechanical alignment."
        )

    if voltage < 205:

        recommendations.append(
            "Voltage instability detected. Inspect power supply."
        )

    if pressure > 40:

        recommendations.append(
            "Pressure exceeds safe threshold. Inspect hydraulic system."
        )

    if runtime_hours > 250:

        recommendations.append(
            "Equipment runtime is high. Schedule preventive maintenance."
        )

    if not recommendations:

        recommendations.append(
            "Equipment operating normally."
        )

    return recommendations