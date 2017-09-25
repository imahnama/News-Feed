import requests, json
def add_posts(title, body):
    url = "http://34.207.10.230:3000/posts/"
    post = {"title": title, "body": body}
    response = requests.post(url, data = json.dumps(post))
    data  = json.loads(response.text)

    new_url = url + data['id']
    return new_url #json.dumps({'url': new_url})
