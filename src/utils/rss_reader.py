from datetime import datetime

import feedparser


def parse_rss_feed(url):
    """Parses an RSS feed and returns a list of articles."""
    articles = []
    feed = feedparser.parse(url)

    if feed.bozo:
        print(f"Error in obtaining feed from {url}")
        return []

    for entry in feed.entries:
        published_at = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            try:
                published_at = datetime(*entry.published_parsed[:6])
            except TypeError as e:
                print(f"Error parsing date for {entry.title}: {e}")
        articles.append({
            "title": entry.title,
            "summary": entry.get("summary", ""),
            "url": entry.link,
            "source": feed.feed.title,
            "published_at": published_at,
            "description": entry.get("description", ""),
        })
    return articles
