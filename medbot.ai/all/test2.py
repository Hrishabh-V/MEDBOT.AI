
import infermedica

# Set up Infermedica API credentials
infermedica_app_id = 'YOUR_APP_ID'
infermedica_app_key = 'YOUR_APP_KEY'

# Create an instance of the Infermedica API
api = infermedica.API(app_id=infermedica_app_id, app_key=infermedica_app_key)

# Function to collect user symptoms
def collect_symptoms():
    symptoms = []
    while True:
        symptom = input("Enter a symptom (or 'done' to finish): ")
        if symptom.lower() == 'done':
            break
        symptoms.append(symptom)
    return symptoms

# Function to predict diseases and recommend medicines
def predict_diseases(symptoms):
    # Create a request for the diagnosis
    request = infermedica.Diagnosis(sex='male', age=30)
    for symptom in symptoms:
        request.add_symptom(symptom, 'present')

    # Get the diagnosis result
    response = api.diagnosis(request)

    # Print the predicted diseases
    print("Predicted diseases:")
    for condition in response.conditions[:3]:
        print(condition.name, condition.probability)

    # Get treatment recommendations for the most probable disease
    top_condition = response.conditions[0]
    treatment = api.get_treatment(top_condition.id)

    # Print the recommended medicines
    print("Recommended medicines:")
    for item in treatment.recommended_treatments:
        print(item.name)

# Collect symptoms from the user
user_symptoms = collect_symptoms()

# Predict diseases and recommend medicines
predict_diseases(user_symptoms)