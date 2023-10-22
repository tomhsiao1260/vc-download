import os
import requests
from PIL import Image
import numpy as np
from tqdm import tqdm
from config import username, password
from requests.auth import HTTPBasicAuth

segment_id = '20230503225234'
url_template = f'http://dl.ash2txt.org/full-scrolls/Scroll1.volpkg/paths/{segment_id}/layers/{{:02}}.tif'

output_folder = os.path.join(segment_id, 'layers')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def download_image(url, filename):
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return True
    else:
        print(f"Failed to download image {filename}, status code: {response.status_code}")
        return False

def main(start, end, step):
    for i in tqdm(range(start, end, step)):
        url = url_template.format(i)
        filename = os.path.join(output_folder, os.path.basename(url))

        # Check if output image already exists, and if so, skip download and resize
        if os.path.exists(filename):
            print(f"Output image {filename} already exists. Skipping download.")
            continue

        download_image(url, filename)

if __name__ == "__main__":
    # download 00.tif, 01.tif
    main(0, 2, 1) 

