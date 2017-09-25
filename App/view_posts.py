import requests, json
def view_posts():
    url = "http://34.207.10.230:3000/posts/"
    response = requests.get(url)
    message_json = response.text
    return response.text
Add Comment
