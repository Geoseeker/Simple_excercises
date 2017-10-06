import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))

# Call requests.get() to download the file.
# 
# Call open() with 'wb' to create a new file in write binary mode.
# 
# Loop over the Response object’s iter_content() method.
# 
# Call write() on each iteration to write the content to the file.
# 
# Call close() to close the file.