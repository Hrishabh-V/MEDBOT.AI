from src.components.symptom_model import SymptomModel
from src.api_clients.llm_client import GeminiClient
from src.utils.logger import logger


class SymptomCheckerService:
    def __init__(self, symptoms_to_diseases, gemini_api_key=None):
        try:
            logger.debug("Initializing SymptomCheckerService")
            self.model = SymptomModel(symptoms_to_diseases)
            self.llm = GeminiClient(gemini_api_key)
        except Exception as e:
            logger.exception("❌ Failed to initialize SymptomCheckerService: %s", e)
            raise RuntimeError("Service initialization failed") from e

    def check(self, user_symptoms):
        try:
            logger.debug("Checking symptoms: %s", user_symptoms)

            # Validate input
            if not user_symptoms or not isinstance(user_symptoms, (list, set, tuple)):
                logger.warning("Invalid symptoms input: %s", user_symptoms)
                return {
                    "predicted_diseases": [],
                    "llm_response": "⚠️ Please provide a valid list of symptoms."
                }

            try:
                predicted_diseases = self.model.predict(user_symptoms)
            except Exception as e:
                logger.exception("❌ Error in symptom prediction: %s", e)
                return {
                    "predicted_diseases": [],
                    "llm_response": "⚠️ Unable to predict diseases at this moment."
                }

            prompt = (
                f"User reported symptoms: {', '.join(user_symptoms)}. "
                f"Predicted possible diseases: {', '.join(predicted_diseases)}. "
                f"Provide a concise explanation, precautions, and actionable advice."
            )
            logger.debug("Sending prompt to Gemini LLM")

            try:
                llm_response = self.llm.ask(prompt)
            except Exception as e:
                logger.exception("❌ LLM request failed: %s", e)
                llm_response = "⚠️ Unable to fetch advice right now. Please try again later."

            logger.debug("✅ Received response from Gemini LLM")

            return {
                "predicted_diseases": list(predicted_diseases),
                "llm_response": llm_response
            }

        except Exception as e:
            logger.exception("❌ Unexpected error in check(): %s", e)
            return {
                "predicted_diseases": [],
                "llm_response": "⚠️ An unexpected error occurred while checking symptoms."
            }
