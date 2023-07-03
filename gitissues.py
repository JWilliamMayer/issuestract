import requests
import csv

url = "INSERT the url for your git enterprise page here, should end in /issues"
token = "Authentication code here if it is required"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers)
issues = response.json()

csv_file = "issues.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Description", "State"]) 
    for issue in issues:
        writer.writerow([issue["title"], issue["body"], issue["state"]])
