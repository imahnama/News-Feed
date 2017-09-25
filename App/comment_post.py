import requests, json

def comment_post(post_id, title, body):
    root_url = "http://34.207.10.230:3000/posts/" + str(post_id) + "/comments"
    comment = {"title":title, "body":body}
    response = requests.post(root_url, data = json.dumps(comment))
    data = json.loads(response.text)
    comment_url = root_url + str(data['id'])
    return comment_url
