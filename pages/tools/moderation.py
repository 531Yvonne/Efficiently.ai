import requests
import os
from dotenv import load_dotenv
load_dotenv()


def moderate_text(text_to_moderate):
    url = "https://api.openai.com/v1/moderations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }
    data = {
        "input": text_to_moderate
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        # Get the violation flag
        violation_flag = response.json()["results"][0]["flagged"]

        # Extract the 'categories' dictionary from the result
        categories_dict = response.json()['results'][0]['categories']

        # Filter the categories with a value of True
        true_categories = [category for category,
                           value in categories_dict.items() if value]
        return {"flag": violation_flag, "content": true_categories}

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
