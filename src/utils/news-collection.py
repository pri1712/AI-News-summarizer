from datetime import datetime
import feedparser
import requests
import os


def get_news_from_rss(url):
    articles = []
    feed = feedparser.parse(url)
    if feed.bozo:
        print("Error in obtaining feed")
        return []

    for entry in feed.entries:
        published_at = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            try:
                published_at = datetime(*entry.published_parsed[:6])
            except TypeError as e:
                print(f"Error parsing date: {e}")
                published_at = None

        articles.append({
            "title": entry.title,
            "summary": entry.get("summary", ""),
            "url": entry.link,
            "source": feed.feed.title,
            "published_at": published_at
        })
    print(articles)

    # Log articles to file in a readable format
    with open("output.txt", "a") as file:
        for article in articles:
            file.write(f"Title: {article['title']}\n")
            file.write(f"Summary: {article['summary']}\n")
            file.write(f"URL: {article['url']}\n")
            file.write(f"Source: {article['source']}\n")
            file.write(f"Published at: {article['published_at']}\n\n")
    return articles


def get_news_from_api(url, key):
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
    print(f"API response status code: {response.status_code}")
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print(f"Error fetching news from API: {response.status_code}")
        return []


def main():
    all_articles = []
    rss_feeds = [
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://www.theguardian.com/uk/rss",
        "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/americas/rss.xml",
        "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/breaking_news/rss.xml",
        "https://edition.cnn.com/sitemap/news.xml",
        "http://rss.cnn.com/rss/cnn_world.rss",
        "https://moxie.foxnews.com/google-publisher/world.xml"
    ]

    for rss_feed in rss_feeds:
        articles_from_feed = get_news_from_rss(rss_feed)
        all_articles.extend(articles_from_feed)


    newsapi_key = os.getenv("NEWSAPI_KEY")
    if newsapi_key:
        newsapi_url = "https://newsapi.org/v2/top-headlines"
        articles_from_api = get_news_from_api(newsapi_url, newsapi_key)
        all_articles.extend(articles_from_api)
    else:
        print("No NEWSAPI_KEY found in environment variables")




if __name__ == '__main__':
    main()
