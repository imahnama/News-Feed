import requests, json
def view_posts():
    url = "http://34.207.10.230:3000/posts/"
    response = requests.get(url)
    message_json = response.text
    return json.dumps(json.loads(message_json), indent=4, separators=(',', ': '))
