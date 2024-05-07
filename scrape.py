import requests
from bs4 import BeautifulSoup


def scrape():
# Send a GET request to the page
    test_url = 'https://roadtonationals.com/results/teams/gymnast/2024/66/32075'
    response = requests.get(test_url)

    if response.status_code == 200: # success
        # Step 4.3: Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 4.4: Extract specific data
        # Example: Extract table data for meet results
        results_table = soup.find('table', class_='results-table')  # Adjust based on structure
        if results_table:
            rows = results_table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                data = [col.get_text().strip() for col in columns]
                print(data)
        else:
            print("No table")
    else:
        print("Failed to retrieve the webpage.")