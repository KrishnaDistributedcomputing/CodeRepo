# azure_service_retirements.py
 
 
This script fetches the Azure retirements feed and generates an HTML document with a list of retired Azure services, along with their retirement date. To run the script, simply execute it in a Python environment.

The script uses the following libraries:
- `re`: provides support for regular expressions
- `requests`: makes HTTP requests to fetch the feed
- `feedparser`: parses the feed into a structured format
- `datetime`: provides support for date and time functions

The script performs the following steps:
1. Defines the URL of the Azure retirements feed
2. Fetches the feed using the `requests` library
3. Parses the feed into a structured format using the `feedparser` library
4. Sorts the feed entries by `lastBuildDate` using the `sorted` function and the `datetime` library
5. Generates an HTML document with hyperlinks to the title of each entry, along with its retirement date
6. Uses regular expressions to extract the date from the title and adds it below the title in the HTML document
7. Prints the HTML document to the console

You can customize the output by modifying the HTML template in the script. You can also change the regular expression used to extract the date if the format of the feed titles changes.

