import os
from utils.rss_reader import parse_rss_feed
from utils.api_reader import fetch_news_from_api
from utils.summarizer import summarize_text
from utils.utility import log_to_file

def main():
    rss_feeds = [
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://www.theguardian.com/uk/rss",
        "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/americas/rss.xml",
        "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/breaking_news/rss.xml",
        "http://rss.cnn.com/rss/cnn_world.rss",
        "https://moxie.foxnews.com/google-publisher/world.xml",
    ]

    all_articles = []
    for rss_feed in rss_feeds:
        """RSS feed related actions"""
        articles = parse_rss_feed(rss_feed)
        all_articles.extend(articles)

    newsapi_key = os.getenv("NEWSAPI_KEY")
    if newsapi_key:
        """NEWS API related actions"""
        newsapi_url = "https://newsapi.org/v2/top-headlines"
        api_articles = fetch_news_from_api(newsapi_url, newsapi_key)
        all_articles.extend(api_articles)


    for article in all_articles:
        try:
            """Logging"""
            summarized = summarize_text(article["description"])
            log_to_file("output.txt", f"Title: {article['title']}\nSummary: {summarized}\n")
        except Exception as e:
            print(f"Error summarizing article: {e}")

if __name__ == "__main__":
    main()
