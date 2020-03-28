import requests
import os
from tqdm import tqdm
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup as bs


# urlparse() function parses a URL into six components,
# we just need to see if the netloc (domain name) and scheme (protocl) are there.
def is_url_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# returns all images url, that contains in url
def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
    image_urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        image_url = img.attrs.get("src")
        if not image_url:
            continue
        image_url = urljoin(url, image_url)
        try:
            pos = image_url.index("?")
            image_url = image_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_url_valid(image_url):
            image_urls.append(image_url)
    return image_urls


# Downloads a file given an URL and puts it in the folder `pathname`
def download(url, pathname):
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def load(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        download(img, path)
