import os
import requests
import shutil
from urllib.parse import urljoin
import bs4

url = 'https://stevemorse.org/8086/'

# Making a new folder
folder_name = '8086'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Scraping information
for p in range(1, 5):
    page_url = urljoin(url, str(p) + '.jpg')
    print('Downloading Page %s.....' % page_url)
    
    try:
        res = requests.get(page_url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        image_url = urljoin(url, str(p) + '.jpg')
        print('Downloading image %s.....' % image_url)
        res = requests.get(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()

        with open(os.path.join(folder_name, os.path.basename(image_url)), 'wb') as image_file:
            for chunk in res.iter_content(10000):
                image_file.write(chunk)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading page {page_url}: {e}")
        continue

print('Done...')
