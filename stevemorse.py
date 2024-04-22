import os
import requests

url = 'https://stevemorse.org/8086'

# Making a new folder
folder_name = '8000'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Scraping information for pages from 1001 to 1011
for p in range(1001, 1012):
    print('Downloading Page %s.....' % p)
    page_url = f'{url}/{p}.jpg'
    try:
        res = requests.get(page_url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download page {page_url}: {e}")
        continue

    image_path = os.path.join(folder_name, f'{p}.jpg')
    with open(image_path, 'wb') as image_file:
        image_file.write(res.content)

# Scraping information for pages from 1 to 276
for p in range(1, 277):
    print('Downloading Page %s.....' % p)
    page_url = f'{url}/{p}.jpg'
    try:
        res = requests.get(page_url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download page {page_url}: {e}")
        continue

    image_path = os.path.join(folder_name, f'{p}.jpg')
    with open(image_path, 'wb') as image_file:
        image_file.write(res.content)

print('Done...')
