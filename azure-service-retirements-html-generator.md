# User Guide for Azure Service Retirements Feed Script:

This script is designed to fetch the Azure retirements feed, sort it by date, and generate an HTML document with hyperlinks to the title and date of each entry.

## Requirements:

Python 3.x installed on your system.
Required libraries:
* re
* requests
* feedparser
* datetime

Usage:

Open your preferred IDE or a terminal and create a new Python file.
Copy and paste the script code into the new file.
Save the file with a .py extension.
Run the script and the output will be the generated HTML document.
Explanation of Script Code:

Import required libraries:
The first step is to import the necessary libraries to be used in the script. These are: re, requests, feedparser, and datetime. These libraries allow us to extract and manipulate data from the Azure retirements feed.

Define URL of the Azure retirements feed:
The URL of the Azure retirements feed is defined and stored in the 'url' variable.

Fetch the feed:
The script uses the requests library to fetch the feed by sending an HTTP GET request to the URL defined in the 'url' variable. The feed is then parsed using feedparser and stored in the 'feed' variable.

Sort the feed entries by lastBuildDate:
The script sorts the feed entries by lastBuildDate using the sorted() function and the key parameter, with lambda function to extract the datetime from the 'updated' attribute of each feed entry.

Generate HTML document with hyperlinks to the title and date:
The script generates an HTML document by looping through the sorted entries and using string formatting to create hyperlinks to the title and date of each entry. It extracts the date from the title using regular expressions and adds it below the title.

Close the HTML document:
After looping through all the sorted entries, the script closes the HTML document.

Print the HTML document:
The final step is to print the generated HTML document to the console using the print() function.

That's it! With this script, you can easily keep track of Azure service retirements and their dates. You can also modify it to fit your specific needs.
