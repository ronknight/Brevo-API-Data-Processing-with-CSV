import os
import csv
import json
import requests
from dotenv import load_dotenv
from datetime import date, datetime  # Import both date and datetime


def process_csv_data(csv_file):
  """
  Processes data from a CSV file and sends it to the Brevo API endpoint.

  Args:
      csv_file (str): Path to the CSV file.
  """
  # Load environment variables from .env file
  load_dotenv()
  base_url = os.getenv("BREVO_API_URL")
  api_key = os.getenv("BREVO_API_KEY")

  today = date.today().strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD

  success_log = open("api_success_log.txt", "a")
  error_log = open("api_log_error.txt", "a")  # Open error log file for appending

  with open(csv_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # Extract data from each row
      email = row["email"]
      fname = row.get("FNAME", "")
      lname = row.get("LNAME", "")
      # ... Extract other data from row as needed ...
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


      # Build payload dictionary
      payload = {
          "email": email,
          "includeListIds": [13],
          "redirectionUrl": "https://www.4sgm.com/category/422/Thank-You.html?utm_source=brevo&utm_campaign=2024-03-batch1-C&utm_medium=email",
          "templateId": 43,
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
        url = f"{base_url}/v3/contacts/doubleOptinConfirmation"  # Combine base URL with endpoint
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        # Successful connection - log data
        success_log.write(f"{timestamp} - Sent data for email: {email}\t")
        success_log.write(f"Payload: {payload}\n")
        print(f"Successfully sent data for email: {email}")

      except requests.exceptions.RequestException as e:
          error_message = f"Error sending data for email: {email} - {e}"
          print(error_message)  # Print to console for visibility
          error_log.write(f"{timestamp} - {error_message}\n")

    success_log.close()
    error_log.close()  # Close the error log file

if __name__ == "__main__":
  csv_file = "data.csv"  # Replace with your CSV file path
  process_csv_data(csv_file)