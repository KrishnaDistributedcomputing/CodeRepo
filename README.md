## Azure Service Retirements Python Script User Guide
**Overview**
The Azure Service Retirements Python script is a simple tool that fetches a feed of retired Azure services from Microsoft's website and generates an output with hyperlinks to the title of each entry along with its retirement date.

Requirements
Python 3
re library
requests library
feedparser library
datetime library

To install the required libraries, you can run the following command:

`` python
pip install requests feedparser
`` 
Usage
To use the script, follow these steps:

Open your terminal and navigate to the directory where the script is saved.
Run the script by executing the following command:
`` python
python azure_service_retirements.py
```
The script will fetch the Azure retirements feed and generate an output with hyperlinks to the title of each entry along with its retirement date. The output will be printed to the console.

**Customization**
You can change the regular expression used to extract the retirement date from the feed entries by editing the match regular expression pattern in the script. This pattern is used to search for a date string in the title of each feed entry. If the pattern does not match the date format in the feed, the date will not be displayed in the output.

**Conclusion**
The Azure Service Retirements Python script is a simple tool that can help you keep track of retired Azure services. With a few simple modifications, you can customize the output to suit your needs.



# Azure Service Retirements Script User Manual for HTML Generation
This script fetches the Azure retirements feed and generates an HTML document with a list of retired Azure services, along with their retirement date.

## Requirements
The script requires Python 3 to run. In addition, the following libraries are used and must be installed:

re: provides support for regular expressions
requests: makes HTTP requests to fetch the feed
feedparser: parses the feed into a structured format
datetime: provides support for date and time functions
To install the libraries, run the following command:

 
`` python
pip install requests feedparser
``
 
Usage
To run the script, simply execute it in a Python environment by running the following command in your terminal:

`` python
python azure_service_retirements_html.py
`` 
## Function of the script
The script will fetch the Azure retirements feed and generate an HTML document with hyperlinks to the title of each entry, along with its retirement date. The output will be printed to the console.

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

## Customization
You can customize the output by modifying the HTML template in the script. You can also change the regular expression used to extract the date if the format of the feed titles changes.

To modify the HTML template, simply edit the html variable in the script. You can add or remove HTML tags and modify the style and layout of the output.

To change the regular expression used to extract the date, you can edit the match regular expression pattern in the script. This pattern is used to search for a date string in the title of each feed entry. If the pattern does not match the date format in the feed, the date will not be displayed in the output.
