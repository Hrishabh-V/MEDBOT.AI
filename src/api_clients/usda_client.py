import os
import requests
from dotenv import load_dotenv
from src.utils.logger import logger
from src.exception.exception_handler import handle_exception   

load_dotenv()
USDA_API_KEY = os.getenv("USDA_API_KEY", "YOUR_USDA_API_KEY")
USDA_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"


def get_nutrient_info(food_name: str) -> str:
    """
    Query USDA API for nutrient info.
    """
    try:
        logger.debug(f"Fetching USDA info for: {food_name}")
        params = {"api_key": USDA_API_KEY, "query": food_name}
        resp = requests.get(USDA_URL, params=params)

        if resp.status_code != 200:
            logger.error(f"USDA API error: {resp.status_code}")
            return f"⚠️ USDA API error (status {resp.status_code})"

        data = resp.json()
        foods = data.get("foods", [])
        if not foods:
            logger.warning(f"No USDA results for {food_name}")
            return f"❌ No information found for {food_name}"

        item = foods[0]
        desc = item.get("description", "")
        brand = item.get("brandOwner", "")
        nutrients = item.get("foodNutrients", [])

        logger.info(f"USDA data found for {food_name}: {desc}")

        lines = [f"🍽 {desc} ({brand})"]
        for n in nutrients[:5]:
            lines.append(f"- {n['nutrientName']}: {n['value']} {n.get('unitName','')}")
        return "\n".join(lines)

    except Exception as e:
        return handle_exception(e, context=f"fetching USDA info for {food_name}")
