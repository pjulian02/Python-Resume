import constants
import urllib
import requests

def shorten_url(url, name):
    key = constants.CUTTLY_API_KEY
    url = urllib.parse.quote('https://stackoverflow.com/questions/56995350/best-practices-python-where-to-store-api-keys-tokens')
    data = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, url)).json()

    print(data["url"]["shortLink"])
