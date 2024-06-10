# Rest of the common bot-related code
import requests

url = ""
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print(response.content.decode())
    data = response.json()
    my_variable_value = data['bot_token']
    
    print(my_variable_value)
else:
    print("Error occurred while calling the Python file.")
