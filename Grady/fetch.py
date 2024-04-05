import requests
import csv

# URL of the API
url = "https://quests.nonlinearmedia.org/foothill/research/grady/php/show_log.php"

# Make a GET request to fetch the data
response = requests.get(url)
if response.status_code == 200:
    # Assuming the data is comma-separated and each new line represents a new row
    data = response.text.split('\n')

    # Specify the CSV file to write the data to
    csv_file_path = 'Grady/grady_data.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        for row in data:
            # Assuming each row is comma-separated, split it into columns
            columns = row.split(',')
            writer.writerow(columns)
    print(f"Data successfully saved to {csv_file_path}")
else:
    print("Failed to fetch the data from the website")