import requests

def get_url(api_url):

    URL = api_url
    r = requests.get(url = URL)
    data = r.json()

    gw = data['data']['controller_gateway']
    print(gw)

def post_url(api_url, data):
    r = requests.post(url = api_url, data = data)
    pastebin_url = r.text
    print("The Pastebin URL is:%s"%pastebin_url)

curl -H "Content-type: application/json" -X POST http://localhost:5000/devices -d ''
