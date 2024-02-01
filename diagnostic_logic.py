from diagnosis import diagnoses

def check_symptoms(symptom_responses, current_diagnosis):
    # Check if all the symptoms related to the current diagnosis are confirmed
    relevant_symptoms = diagnoses[current_diagnosis]
    return all(symptom_responses.get(symptom, False) for symptom in relevant_symptoms)

def guess_diagnosis(symptom_responses):
    diagnosis_scores = {diagnosis: 0 for diagnosis in diagnoses.keys()}
    for symptom, response in symptom_responses.items():
        if response:  # If the symptom is confirmed
            for diagnosis, symptoms in diagnoses.items():
                if symptom in symptoms:
                    diagnosis_scores[diagnosis] += 1
    # Find the diagnosis with the highest score
    final_diagnosis = max(diagnosis_scores, key=diagnosis_scores.get)
    return final_diagnosis if diagnosis_scores[final_diagnosis] > 0 else "No diagnosis could be made based on the provided symptoms."
