import csv
import feedparser
import requests
import re
from datetime import datetime

url = 'https://azurecomcdn.azureedge.net/en-us/updates/feed/?query=retire'

response = requests.get(url)

feed = feedparser.parse(response.content.decode('utf-8'))

# Sort the feed entries by lastBuildDate
sorted_entries = sorted(feed.entries, key=lambda x: datetime.strptime(x.updated, '%a, %d %b %Y %H:%M:%S %z'), reverse=True)

# Generate list of retired Azure services with their retirement date
with open('retired_azure_services.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Title', 'Date', 'Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for entry in sorted_entries:
        title = entry.title
        match = re.search(r'(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{1,2},\s+\d{4}|\w+\s+\d{4})', title)
        if match:
            date_str = match.group(1)
        else:
            date_str = ""

        writer.writerow({'Title': title, 'Date': date_str, 'Link': entry.link})
