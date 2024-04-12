import os
import csv
import json
import requests
from dotenv import load_dotenv
from datetime import date, datetime
import tqdm
import time

def process_csv_data(csv_file):
    """
    Processes data from a CSV file and sends it to the Brevo API endpoint.
    """
    # Load environment variables
    load_dotenv()
    base_url = os.getenv("BREVO_API_URL")
    api_key = os.getenv("BREVO_API_KEY")

    today = date.today().strftime("%Y-%m-%d")  
    first_iteration = True  

    # Open log files 
    success_log = open("api_success_log.txt", "a")
    error_log = open("api_log_error.txt", "a")  

    # Process the CSV file
    with open(csv_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for _ in reader)  # Count rows

    with open(csv_file, "r") as csvfile: 
        reader = csv.DictReader(csvfile)

        with tqdm.tqdm(total=total_rows, desc="Processing Contacts", dynamic_ncols=True) as progress_bar: 
            for row in reader: 
                if first_iteration:
                    time.sleep(0)  
                    first_iteration = False  
                else:
                    time.sleep(60) 

                # Extract data
                email = row["email"]
                fname = row.get("FNAME", "")
                lname = row.get("LNAME", "")
                # ... Extract other data from row as needed ...

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Build payload dictionary
                payload = {
                    "email": email,
                    "includeListIds": [13],
                    "redirectionUrl": "https://www.4sgm.com/category/422/Thank-You.html?utm_source=brevo&utm_campaign=2024-03-batch1-E&utm_medium=email",
                    "templateId": 46,
                    "attributes": {
                        "FNAME": fname,
                        "LNAME": lname,
                        # ... Add other attributes from row data ...
                    },
                    "excludeListIds": [6],
                }

                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'api-key': api_key
                }

                try:
                    url = f"{base_url}/v3/contacts/doubleOptinConfirmation"  
                    response = requests.post(url, headers=headers, json=payload)
                    response.raise_for_status()

                    # Successful connection - log data
                    success_log.write(f"{timestamp} - Sent data for email: {email}\t")
                    success_log.write(f"Payload: {payload}\n")
                    print(f"Successfully sent data for email: {email}")

                except requests.exceptions.RequestException as e:
                    error_message = f"Error sending data for email: {email} - {e}"
                    print(error_message) 
                    error_log.write(f"{timestamp} - {error_message}\n")

                progress_bar.update(1)  # Update progress bar in-place

    success_log.close()
    error_log.close()  

if __name__ == "__main__":
    csv_file = "data.csv"  # Replace with your CSV file path
    process_csv_data(csv_file)