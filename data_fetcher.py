import requests


API_KEY = "5xmjyS7QSqo8Bb0AsHDw6w==1QzdbDyMawRuJvlb"
def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals  """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"


    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(url,headers=headers)
    return response.json()
