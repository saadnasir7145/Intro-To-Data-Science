#17/8/2023
#fa20-bse-059
#Assignment1-web scraping
#saad nasir
#

import requests
from bs4 import BeautifulSoup
import time
import openpyxl

# Function to scrape movie details from IMDB
def scrape_movie_details(url):
    # Fetch the webpage
    response = requests.get(url)
    time.sleep(1)  # Sleep for 1 second to avoid overloading the server

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title and rating
        title = soup.find('h1').get_text(strip=True)
        rating = soup.find('span', itemprop='ratingValue').get_text(strip=True)

        return {'Title': title, 'Rating': rating}
    else:
        print(f"Failed to fetch {url}")
        return None

# List of new movie URLs
movie_urls = [
    'https://www.imdb.com/title/tt0167260/',  # The Lord of the Rings: The Two Towers
    'https://www.imdb.com/title/tt1375666/',  # Inception
    'https://www.imdb.com/title/tt4154796/',  # Avengers: Endgame
    'https://www.imdb.com/title/tt0088763/',  # Back to the Future
    'https://www.imdb.com/title/tt4154756/'   # Avengers: Infinity War
]

# Create a workbook and add a sheet
wb = openpyxl.Workbook()
ws = wb.active

# Add headers to the sheet
ws.append(['Title', 'Rating'])

# Iterate through movie URLs and scrape details
for url in movie_urls:
    movie_details = scrape_movie_details(url)
    if movie_details:
        ws.append([movie_details['Title'], movie_details['Rating']])

# Save the workbook to an Excel file
excel_file_path = 'new_movie_data.xlsx'
wb.save(excel_file_path)

print(f"Data has been successfully exported to {excel_file_path}"

#Question 2

import requests
from bs4 import BeautifulSoup

# Function to scrape 'timeanddate' website
def scrape_time_and_date(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting the shared birthdate information
        birthdate_info = soup.find('div', class_='otd-box-content').text.strip()
        return birthdate_info
    else:
        print(f"Failed to fetch {url}")
        return None

# Function to scrape 'britannica' website
def scrape_britannica(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting important events from Britannica
        events = []
        for event in soup.find_all('div', class_='md-4'):
            events.append(event.text.strip())
        return events
    else:
        print(f"Failed to fetch {url}")
        return None

# URLs of the specified websites
time_and_date_url = 'https://www.timeanddate.com/on-this-day'
britannica_url = 'https://www.britannica.com/on-this-day'

# Scraping information from 'timeanddate' website
shared_birthdate_info = scrape_time_and_date(time_and_date_url)

# Scraping information from 'britannica' website
britannica_events = scrape_britannica(britannica_url)

# Writing information to a text file
output_file_path = 'birthdate_info.txt'
with open(output_file_path, 'w') as file:
    file.write("Who you share your birthdate with (from 'timeanddate' website):\n")
    file.write(f"{shared_birthdate_info}\n\n")

    file.write("Important event(s) happened on your birthdate (from 'britannica' website):\n")
    for event in britannica_events:
        file.write(f"- {event}\n")

print(f"Information has been successfully written to {output_file_path}")
