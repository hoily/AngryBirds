import requests
import urllib.parse as urllib

API_URL = "http://sentiment.vivekn.com/api/text/"


def get_analysis(text):
    encoded_text = urllib.quote(text, safe='')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    request = requests.post(API_URL,
                            data="txt={}".format(encoded_text),
                            headers=headers)
    return(request.json()["result"])
