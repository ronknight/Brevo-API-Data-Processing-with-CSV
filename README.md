<p><a target="_blank" href="https://app.eraser.io/workspace/427E9mL2QrH2rpHE9SVm" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

<h1 align="center"><a href="https://github.com/ronknight/Brevo-API-Data-Processing-with-CSV">Brevo API Data Processing with CSV</a></h1>
<h4 align="center">This project automates sending data from a CSV file to the Brevo API for double opt-in confirmation.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/Brevo-API-Data-Processing-with-CSV/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/Brevo-API-Data-Processing-with-CSV/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#setup">Setup</a> •
  <a href="#usage">Usage</a> •
  <a href="#explanation">Explanation</a> •
  <a href="#logs">Logs</a> •
  <a href="#security">Security</a> •
  <a href="#notes">Notes</a> •
  <a href="#diagrams">Diagrams</a> •
</p>

---

## Features:
Iterates through a CSV file, extracting email and other relevant data.
Constructs a payload dictionary based on extracted data.
Sends POST requests to the Brevo API endpoint for each row in the CSV.
Logs successful API connections and sent data to a text file.
Uses python-dotenv to securely manage API key and base URL from a .env file.

## Requirements:
- Python 3.x
- requests library (pip install requests)
- python-dotenv library (pip install python-dotenv)
## Setup:
1. Create a virtual environment (recommended) for isolated project dependencies.
2. Install required libraries: pip install requests python-dotenv
3. Create a CSV file with headers matching the data extraction logic (e.g., email, FNAME, LNAME).
4. Create a .env file in your project directory and add the following lines, replacing placeholders with your actual values:
```bash
BREVO_API_KEY=your_api_key
BREVO_API_URL=https://api.brevo.com
```
## Usage:
Replace your_data.csv in the script with the path to your CSV file.
Run the script: 

```bash
python main.py
```
## Explanation:
The script iterates through each row in the CSV file, extracts data like email, first name, and last name. It then builds a payload dictionary according to the Brevo API specifications and sends a POST request using the requests library.

## Success Log:

The script logs successful API connections with email addresses and the corresponding sent data to a file named api_success_log.txt.

## Security:
This version uses python-dotenv to store sensitive information like the API key and base URL in a separate .env file, which is not included in version control.

## Note:
Modify the script's data extraction logic to match your specific CSV format.
Error handling is included for catching potential request exceptions.
This project provides a basic framework for sending data from a CSV file to the Brevo API. You can customize it further based on your specific needs.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Brevo API Data Processing with CSV-1.eraserdiagram" data-element-id="fexIafQDXbKbDqreABvuB"><img src="/.eraser/427E9mL2QrH2rpHE9SVm___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----45e0b0ce114090220152bb265f71f347-Brevo-API-Data-Processing-with-CSV.png" alt="" data-element-id="fexIafQDXbKbDqreABvuB" /></a>
<a href="/README-Brevo API Data Processing with CSV-2.eraserdiagram" data-element-id="2ruRMjC1k-AFuyIGnXxv8"><img src="/.eraser/427E9mL2QrH2rpHE9SVm___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----7c7cfac86f5478b012df28f5e7d5576b-Brevo-API-Data-Processing-with-CSV.png" alt="" data-element-id="2ruRMjC1k-AFuyIGnXxv8" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/427E9mL2QrH2rpHE9SVm --->