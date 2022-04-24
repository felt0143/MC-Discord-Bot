import os
import random
import giphy_client
from giphy_client.rest import ApiException
from dotenv import load_dotenv

load_dotenv()
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

giphy = giphy_client.DefaultApi()


def search(query, number_of_results=1):
    try:
        response = giphy.gifs_search_get(GIPHY_API_KEY, query, limit=number_of_results)
    except ApiException as exception:
        print(f'Exception when calling DefaultApi->gits_search_get: {exception}')

    return_index = random.randint(0, number_of_results)
    return_index = min(return_index, len(response.data) - 1)
    return response.data[return_index].embed_url
