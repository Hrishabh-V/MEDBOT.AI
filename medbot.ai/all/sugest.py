
import requests
from bs4 import BeautifulSoup

def get_medicine_info(medicine_name):
    # Replace 'website_url' with the actual URL of the website you want to scrape
    website_url = 'https://www.drugs.com/'
    search_url = f'{website_url}/search.php?searchterm={medicine_name}'
    
    # Send a GET request to the search URL
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information from the webpage
        medicine_info = []
        
        # Example: Extracting the medicine name, description, and dosage information
        name = soup.select_one('.medicine-name')  # Modify the CSS selector according to the website's structure
        
        if name:
            name = name.text.strip()
        
        description = soup.select_one('.medicine-description')
        
        if description:
            description = description.text.strip()
        
        dosage = soup.select_one('.medicine-dosage')
        
        if dosage:
            dosage = dosage.text.strip()
        
        medicine_info.append({'Name': name, 'Description': description, 'Dosage': dosage})
        
        return medicine_info
    else:
        print('Error: Unable to fetch medicine information.')
        return None

# Example usage
medicine_name = input("Enter the medicine name: ")
medicine_info = get_medicine_info(medicine_name)

if medicine_info:
    print(f"Medicine: {medicine_info[0]['Name']}")
    print(f"Description: {medicine_info[0]['Description']}")
    print(f"Dosage: {medicine_info[0]['Dosage']}")