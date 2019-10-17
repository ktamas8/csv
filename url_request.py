import requests

def get_url(api_url):

    URL = api_url
    r = requests.get(url = URL)
    data = r.json()

    gw = data['data']['controller_gateway']
    print(gw)

def post_url():
    print("test_post")
