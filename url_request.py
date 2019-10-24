import requests

def get_url(api_url):

    URL = api_url
    r = requests.get(url = URL)
    data = r.json()

    gw = data['data']['controller_gateway']
    print(gw)

def post_url(api_url, json_data):
    r = requests.post(url = api_url, data = json_data)
    pastebin_url = r.text
    print("The Pastebin URL is:%s"%pastebin_url)
