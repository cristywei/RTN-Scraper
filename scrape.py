import time # webpage loading time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd # table generation?

def read_list(table):
    '''
    goal is to extract the values used in scrape to get scores
    determine the season year, team_code, and gymnast_ID which will be hardcoded into the data
    '''
    for x, y, z in table:
        codes = [x, y, z for x, y, z in table]
    return codes

def scrape(year, team_code, gymnast_ID):
    firefox_options = Options()
    firefox_options.add_argument('--headless')  # headless mode gets rid of GUI
    geckodriver_path = "drivers/geckodriver" # put drivers in driver folder
    service = Service(geckodriver_path)

    driver = webdriver.Firefox(service=service, options=firefox_options)

    driver.get('https://roadtonationals.com/results/teams/gymnast/2024/66/31516' + year + team_code + gymnast_ID)  # URL

    # Wait for dynamic content to load
    time.sleep(10)  # Adjust sleep time if needed

    # Get the page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table_element = driver.find_element(By.CLASS_NAME, 'ReactTable')  # Adjust if needed

    # Get the table headers
    header_elements = table_element.find_elements(By.XPATH, './/div[@role="columnheader"]/div')
    headers = [header.text for header in header_elements if header.text != ""]

    # Get the table rows
    row_elements = table_element.find_elements(By.XPATH, './/div[@role="rowgroup"]')

    # Extract data from rows
    table_data = []

    for row in row_elements:
        # Find all cells in the row
        cell_elements = row.find_elements(By.XPATH, './/div[@role="gridcell"]')
        row_data = [cell.text for cell in cell_elements]
        table_data.append(row_data)

    print(table_data)
    print(headers)

    driver.quit()

'''
    # Extract data as needed
    results_table = soup.find('table', class_='results-table')
    if results_table:
        rows = results_table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            data = [col.get_text().strip() for col in columns]
            print(data)
    else:
        print(driver.page_source)
'''

'''
def get_team_code(team):
    team_table = ['Air Force', 'Alabama', 'Alaska', 'Arizona', 'Arizona State', 'Arkansas', 'Auburn', 'Ball State', 'Boise State', 'Bowling Green', 'Bridgeport', 'Brockport', 'Brown', 'BYU', 'California', 'Centenary College', 'Central Michigan', 'Cornell', 'Cortland State', 'Denver', 'Eastern Michigan', 'Fisk', 'Florida', 'George Washington', 'Georgia', 'Greenville', 'Gustavus Aldophus', 'Hamline', 'Illinois', 'Illinois State', 'Iowa', 'Iowa State', 'Ithaca College', 'Kent State', 'Kentucky', 'Lindenwood', 'LIU', 'LSU', 'Maryland', 'Michigan', 'Michigan State', 'Minnesota', 'Missouri', 'Nebraska', 'New Hampshire', 'North Carolina', 'North Carolina State', 'Northern Illinois', 'Ohio State', 'Oklahoma', 'Oregon State', 'Penn State', 'Pennsylvania', 'Pittsburgh', 'Rhode Island College', 'Rutgers', 'S.E. Missouri', 'Sacramento State', 'San Jose State', 'Simpson', 'Southern Conn.', 'Southern Utah', 'Springfield College', 'Stanford', 'Temple', 'Texas Women\'s', 'Towson', 'UC Davis', 'UCLA', 'Ursinus College', 'Utah', 'Utah State', 'UW-Eau Claire', 'UW-LaCross', 'UW-Oshkosh', 'UW-Stout', 'UW-Whitewater', 'Washington', 'West Chester', 'West Virginia', 'Western Michigan', 'William & Mary', 'Winona State', 'Yale']
    code = team_table.index(team)
    print(code)
'''