# used library
import requests

# parameters to get specific questions
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 9
}

# get questions by the parameters from the database
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]


# get your questions at: https://opentdb.com/api_config.php
