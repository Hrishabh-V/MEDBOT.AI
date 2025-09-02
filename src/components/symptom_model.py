from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import NotFittedError
from src.utils.logger import logger


class SymptomModel:
    def __init__(self, symptoms_to_diseases):
        logger.debug("Initializing SymptomModel")
        self.vectorizer = CountVectorizer()
        self.label_encoder = LabelEncoder()
        self.classifier = RandomForestClassifier()

        try:
            self.train(symptoms_to_diseases)
        except Exception as e:
            logger.error(f"Error during model initialization/training: {e}")
            raise

    def train(self, symptoms_to_diseases):
        """
        Train the model with a dictionary mapping symptoms to diseases.
        """
        logger.debug("Training SymptomModel with symptoms-to-diseases mapping")
        try:
            if not symptoms_to_diseases or not isinstance(symptoms_to_diseases, dict):
                raise ValueError("symptoms_to_diseases must be a non-empty dictionary")

            symptoms, diseases = [], []
            for symptom, assoc_diseases in symptoms_to_diseases.items():
                if not assoc_diseases:
                    logger.warning(f"Symptom '{symptom}' has no associated diseases. Skipping.")
                    continue
                symptoms.append(symptom)
                diseases.append(', '.join(assoc_diseases))

            if not symptoms or not diseases:
                raise ValueError("No valid symptom-disease pairs found for training")

            X = self.vectorizer.fit_transform(symptoms)
            y = self.label_encoder.fit_transform(diseases)
            self.classifier.fit(X, y)
            logger.debug("Training completed successfully")

        except Exception as e:
            logger.error(f"Error during training: {e}")
            raise

    def predict(self, user_symptoms):
        """
        Predict diseases from user symptoms.
        """
        logger.debug(f"Predicting diseases for user symptoms: {user_symptoms}")
        try:
            if not user_symptoms or not isinstance(user_symptoms, list):
                raise ValueError("user_symptoms must be a non-empty list of strings")

            X_user = self.vectorizer.transform(user_symptoms)
            y_pred_encoded = self.classifier.predict(X_user)
            predicted = self.label_encoder.inverse_transform(y_pred_encoded)

            logger.debug(f"Predicted diseases: {predicted}")
            return predicted

        except NotFittedError:
            logger.error("Model has not been trained. Please train the model before prediction.")
            return ["Model not trained"]
        except ValueError as ve:
            logger.error(f"Invalid input for prediction: {ve}")
            return ["Invalid input"]
        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            return ["Prediction error"]
