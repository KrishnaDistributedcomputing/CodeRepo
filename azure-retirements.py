import re
import requests
import feedparser
from datetime import datetime

url = 'https://azurecomcdn.azureedge.net/en-us/updates/feed/?query=retire'

response = requests.get(url)

feed = feedparser.parse(response.content)

# Sort the feed entries by lastBuildDate
sorted_entries = sorted(feed.entries, key=lambda x: datetime.strptime(x.updated, '%a, %d %b %Y %H:%M:%S %z'), reverse=True)

# Generate list of retired Azure services with their retirement date
for entry in sorted_entries:
    print(f'Title: {entry.title}')
    match = re.search(r'(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{1,2},\s+\d{4}|\w+\s+\d{4})', entry.title)
    if match:
        date_str = match.group(1)
        print(f'Date: {date_str}')
    print(f'Link: {entry.link}')
    print()
