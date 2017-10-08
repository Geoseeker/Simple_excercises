import requests
# Under page pass any page you want
page = 'https://wp.pl'
res = requests.get(page)
res.raise_for_status()
playFile = open('page.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()