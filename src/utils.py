import requests
import os
import json

def get_current_weather(location):
    RAPID_API_KEY = os.getenv("RAPID_API_KEY")
    try:
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q": location}
        print(f"\n>>>> WEATHER API FUNCTION CALL, got the querystring as: {querystring}")
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response_json = response.json()
        print(f"\n>>>> got the RAPID API response as: \n{response_json}")
        return response_json
    except Exception as e:
        raise e

def get_top_headlines(query: str = None, country: str = None, category: str = None):
    """Retrieve top headlines from newsapi.org (API key required)"""

    # prepare headers and search params - default category is 'general'
    base_url = "https://newsapi.org/v2/top-headlines"
    headers = {
        "x-api-key": os.getenv("NEWS_API_KEY")
    }
    params = { "category": "general", "pageSize":1 }
    if query is not None:
        params['q'] = query
    if country is not None:
        params['country'] = country
    if category is not None:
        params['category'] = category

    print(f"\n>>>> NEWS API FUNCTION CALL, got the querystring as: {params}")

    # Fetch from newsapi.org - reference: https://newsapi.org/docs/endpoints/top-headlines
    response = requests.get(base_url, params=params, headers=headers)
    data = response.json()

    if data['status'] == 'ok':
        print(f"Processing {data['totalResults']} articles from newsapi.org")
        return json.dumps(data['articles'])
    else:
        print("Request failed with message:", data['message'])
        return 'No articles found'