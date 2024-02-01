from diagnosis import diagnoses

def check_symptoms(symptom_responses, current_diagnosis):
    # Check if all the symptoms related to the current diagnosis are confirmed
    relevant_symptoms = diagnoses[current_diagnosis]
    return all(symptom_responses.get(symptom, False) for symptom in relevant_symptoms)

def guess_diagnosis(symptom_responses):
    for diagnosis in diagnoses.keys():
        if check_symptoms(symptom_responses, diagnosis):
            return diagnosis
    return "No diagnosis could be made based on the provided symptoms."
