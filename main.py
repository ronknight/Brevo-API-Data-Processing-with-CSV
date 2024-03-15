import os
import csv
import json
import requests
from dotenv import load_dotenv

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

  success_log = open("api_success_log.txt", "a")

  with open(csv_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # Extract data from each row
      email = row["email"]
      fname = row.get("FNAME", "")
      lname = row.get("LNAME", "")
      # ... Extract other data from row as needed ...

      # Build payload dictionary
      payload = {
          "email": email,
          "includeListIds": [13],
          "redirectionUrl": "https://www.4sgm.com/category/422/Thank-You.html",
          "templateId": 41,
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
        success_log.write(f"Sent data for email: {email}\n")
        success_log.write(f"Payload: {payload}\n\n")
        print(f"Successfully sent data for email: {email}")

      except requests.exceptions.RequestException as e:
        print(f"Error sending data for email: {email} - {e}")

  success_log.close()


if __name__ == "__main__":
  csv_file = "data.csv"  # Replace with your CSV file path
  process_csv_data(csv_file)