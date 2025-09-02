from src.components.image_model import classify_image
from src.api_clients.usda_client import get_nutrient_info
from src.utils.logger import logger


class FoodScannerService:
    @staticmethod
    def scan(image_path: str) -> str:
        """
        Scan an image of food, classify it, and fetch USDA nutrient info.
        """
        logger.info("🔍 Scanning image: %s", image_path)

        food_name = classify_image(image_path)
        logger.debug("Predicted food: %s", food_name)   

        if not food_name or "none edible item" in food_name.lower():
            logger.warning("Non-edible item detected")
            return "❌ This item is not edible."

        nutrient_info = get_nutrient_info(food_name)
        logger.info("✅ Nutrient info fetched for: %s", food_name)
        return nutrient_info
