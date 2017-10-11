#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
    #Download the page.
    print('Downloading page {}'.format(url))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')


    #Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            #Download the image.
            print('Downloading image {}'.format(comicUrl))
            res = request.get(comicUrl)
            res.raise_for_status
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url ='http://xkcd.com' + prevLink.get('href')
            continue

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done.')