import time # webpage loading time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd # table generation

def team_code(team):
    team_list = ['Uncommitted', 'Air Force', 'Alabama', 'Alaska', 'Arizona', 'Arizona State', 'Arkansas', 'Auburn', 'BYU', 'Ball State', 'Boise State', 'Bowling Green', 'Bridgeport', 'Brockport', 'Brown', 'California', 'Centenary College', 'Central Michigan', 'Cornell', 'Cortland State', 'Denver', 'Eastern Michigan','Florida', 'George Washington', 'Georgia', 'Gustavus Aldophus', 'Hamline', 'Illinois State', 'Illinois', 'Iowa', 'Iowa State', 'Ithaca College', 'Kent State', 'Kentucky', 'LSU', 'Lindenwood', 'Maryland', 'Michigan', 'Michigan State', 'Minnesota', 'Missouri', 'Nebraska','New Hampshire', 'North Carolina', 'North Carolina State', 'Northern Illinois', 'Ohio State', 'Oklahoma', 'Oregon State', 'Penn State', 'Pennsylvania', 'Pittsburgh', 'Rhode Island College', 'Rutgers', 'S.E. Missouri', 'Sacramento State', 'San Jose State', '', 'Southern Conn.', 'Southern Utah', 'Springfield College', 'Stanford', 'Temple', 'Texas Women\'s', 'Towson', 'UC Davis', 'UCLA',  '', 'Ursinus College', 'Utah', 'Utah State', 'Washington', 'West Chester', 'West Virginia', 'Western Michigan', 'William & Mary', 'Winona State', 'UW-Eau Claire', 'UW-LaCross', 'UW-Oshkosh', 'UW-Stout', 'UW-Whitewater', 'Yale']
    if team == 'Clemson':
        return 163
    elif team == 'LIU':
        return 128
    elif team == 'Fisk':
        return 156
    elif team == 'Greenville':
        return 154
    elif team == 'Talledega':
        return 165
    elif team == 'Utica':
        return 164
    else:
        return team_list.index(team)
    
def get_urls(csv):
    urls = []

    for row in csv:
        year = csv.year()
        team_code = team_code(team)
        gymnast_id = csv.gymnast_ID

        url = 'https://roadtonationals.com/results/teams/gymnast/2024/66/31516/' + year + '/' + team_code + '/' + gymnast_id # URL 

        urls.append(url)
        
    return urls


def scrape(url):
    firefox_options = Options()
    firefox_options.add_argument('--headless')  # headless mode gets rid of GUI
    geckodriver_path = "drivers/geckodriver" # put drivers in driver folder
    service = Service(geckodriver_path)

    driver = webdriver.Firefox(service=service, options=firefox_options)

    get_urls(csv)

    driver.get('url')  # URL

    # Wait for dynamic content to load
    time.sleep(10)  # Adjust sleep time if needed

    # page source, parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table_element = driver.find_element(By.CLASS_NAME, 'ReactTable')  # Adjust if needed

    # headers
    header_elements = table_element.find_elements(By.XPATH, './/div[@role="columnheader"]/div')
    headers = [header.text for header in header_elements if header.text != ""]

    # rows
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

def batch_scrapy():
    return