# Azure Service Retirements Exporter
The [azure_retirements_csv_exporter.py](https://github.com/KrishnaDistributedcomputing/CodeRepo/blob/main/azure_retirements_csv_exporter.py) script is a Python script that retrieves and exports a list of retired Azure services from the Azure updates RSS feed. The output is saved to a CSV file, which can be opened in any spreadsheet program.

## Requirements
Before running the script, ensure that you have the following requirements installed:

* Python 3.x
* requests library (pip install requests)
* feedparser library (pip install feedparser)

## How to Use
* Open a command prompt or terminal window.

* Navigate to the directory where the [azure_retirements_csv_exporter.py](https://github.com/KrishnaDistributedcomputing/CodeRepo/blob/main/azure_retirements_csv_exporter.py) script is located.

* Run the script by typing python azure_service_retirements.py and pressing Enter.

* The script will retrieve the Azure updates RSS feed and sort the entries by the last build date.

* The script will then generate a list of retired Azure services with their retirement date and export the output to a CSV file named "retired_azure_services.csv". Do note the 'Date' at times will have non-date field. This is due to how the XML gets formatted. Please fix the csv file as necessary.

* Once the script completes, open the "retired_azure_services.csv" file in any spreadsheet program (e.g. Microsoft Excel, Google Sheets) to view the list of retired Azure services.

## Troubleshooting
* If you encounter any errors while running the script, ensure that you have the required libraries installed and that your Internet connection is stable.

* If the output CSV file contains gibberish characters, ensure that you have specified the correct encoding in the script (e.g. UTF-8).

* If you need to modify the output CSV file name or location, update the script accordingly before running it.

## Conclusion
The "azure_service_retirements.py" script provides a quick and easy way to retrieve and export a list of retired Azure services. By following the simple steps outlined in this user manual, you can generate a CSV file with the relevant information and use it as needed.
