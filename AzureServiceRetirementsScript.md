# Azure Service Retirements Python Script User Guide
Overview
The Azure Service Retirements Python script is a simple tool that fetches a feed of retired Azure services from Microsoft's website and generates an output with hyperlinks to the title of each entry along with its retirement date. This is a non-HTML version of the script.

## Requirements
* Python 3
* re library
* requests library
* feedparser library
* datetime library

To install the required libraries, you can run the following command:

```python
pip install requests feedparser
```

## Usage
To use the script, follow these steps:

Open your terminal and navigate to the directory where the script is saved.
Run the script by executing the following command:

https://github.com/KrishnaDistributedcomputing/CodeRepo/blob/main/azure-retirements.py
``` python
python azure-retirements.py
```
The script will fetch the Azure retirements feed and generate an output with hyperlinks to the title of each entry along with its retirement date. The output will be printed to the console.

## Customization
You can change the regular expression used to extract the retirement date from the feed entries by editing the match regular expression pattern in the script. This pattern is used to search for a date string in the title of each feed entry. If the pattern does not match the date format in the feed, the date will not be displayed in the output.

## Conclusion
The Azure Service Retirements Python script is a simple tool that can help you keep track of retired Azure services. With a few simple modifications, you can customize the output to suit your needs.
