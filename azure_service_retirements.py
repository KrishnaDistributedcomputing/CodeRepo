# Import required libraries
import re
import requests
import feedparser
from datetime import datetime

# Define URL of the Azure retirements feed
url = 'https://azurecomcdn.azureedge.net/en-us/updates/feed/?query=retire'

# Fetch the feed
response = requests.get(url)
feed = feedparser.parse(response.content)

# Sort the feed entries by lastBuildDate
sorted_entries = sorted(feed.entries, key=lambda x: datetime.strptime(x.updated, '%a, %d %b %Y %H:%M:%S %z'), reverse=True)

# Generate HTML document with hyperlinks to the title and date
html = '<html><head><title>Azure Service Retirements</title></head><body>'
for entry in sorted_entries:
    # Add the hyperlink to the title
    html += f'<p><a href="{entry.link}">{entry.title}</a></p>'
    # Extract the date from the title using regular expressions
    match = re.search(r'(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{1,2},\s+\d{4}|\w+\s+\d{4})', entry.title)
    if match:
        date_str = match.group(1)
        # Add the date below the title
        html += f'<p>Date: {date_str}</p>'
# Close the HTML document
html += '</body></html>'

# Print the HTML document
print(html)
