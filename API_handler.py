import requests
import pandas as pd
from jsonschema import validate, exceptions


schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string", "minLength": 1, "maxLength": 100},
            "thumbnail": {"type": "string", "minLength": 1, "maxLength": 100},
            "thumbnail": {"type": "string", "minLength": 1, "maxLength": 100},
            "game_url": {"type": "string", "minLength": 1, "maxLength": 100},
            "genre": {"type": "string", "minLength": 1, "maxLength": 100},
            "platform": {"type": "string", "enum": ["PC (Windows)"]},
            "publisher": {"type": "string", "minLength": 1, "maxLength": 100},
            "developer": {"type": "string", "minLength": 1, "maxLength": 100},
            "release_date": {"type": "string", "format": "date-time"},
            "freetogame_profile_url": {"type": "string", "minLength": 1, "maxLength": 100},
        },
        "required": ["id","game_url"],
    }
}

url = "https://www.freetogame.com/api/games"

try:
   
    response = requests.get(url)
    response.raise_for_status()
    
    valid_items = []
    corrupted_items = []

    for item in response.json():
        try:
            validate(item, schema["items"])
            valid_items.append(item)
        except exceptions.ValidationError:
            corrupted_items.append(item)

    print("Count of corrupted items:", len(corrupted_items))
    print("Count of valid items:", len(valid_items))

    game_list = pd.json_normalize(valid_items)
    print(game_list)

except requests.exceptions.RequestException as req_err:
    print(f"HTTP request failed: {req_err}")
except exceptions.ValidationError as schema_err:
    print(f"Schema validation failed: {schema_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
