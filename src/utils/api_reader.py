import requests

def fetch_news_from_api(url,key):
    if not key:
        print("API Key is missing!")
        return []

    params = {
        "apiKey": key,
        "language": "en",
        "category": "general",
        "pageSize": 100  # Number of articles.
    }

    response = requests.get(url, params=params)
    #print(f"API response status code: {response.status_code}")
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print(f"Error fetching news from API: {response.status_code}")
        return []