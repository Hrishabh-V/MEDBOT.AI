import requests

def get_nutrient_info(food_name):
    # Replace the URL with the endpoint of the Food Control API
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
    # Replace 'api_key' with the parameter name used by the Food Control API for authentication
    api_key = 'YOUR_API'
    # Set the serving size to 100 grams
    serving_size = 100
    # Make the API request
    params = {
        'api_key': api_key,
        'query': food_name,
        'pageSize': 1,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        if 'foods' in data and len(data['foods']) > 0:
            food = data['foods'][0]
            # Extract nutrient information
            nutrients = food.get('foodNutrients', [])
            calorie_info = 0
            for nutrient in nutrients:
                if nutrient.get('nutrientName') == 'Energy':
                    calorie_info = nutrient.get('value', 0)
                    break
            return f'Calories in {food_name.capitalize()} per {serving_size} grams: {calorie_info}'
        else:
            return f'Could not find {food_name.capitalize()} in the database'
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

# Test the function with a food name
food_name = "burger"
print(get_nutrient_info(food_name))
