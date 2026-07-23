def generate_recommendation(predicted_al):

    ingot = 180
    shots = 40

    wire = max(predicted_al - ingot - shots, 0)

    saving = max(250 - predicted_al, 0)

    return {

        "Predicted_Al": round(predicted_al, 1),

        "Ingot": ingot,

        "Shots": shots,

        "Wire": round(wire, 1),

        "Recovery": 92,

        "Confidence": 94,

        "Saving": round(saving, 1)

    }