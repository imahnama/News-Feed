import requests

def comment_on_post(self,post_id, title, body):
    root_url = "http://34.207.10.230:3000/posts/post_id/comments"
    comment = {"post_id":post_id, "title":title, "body":body}
    response = requests.post(url, data = json.dumps(comment))
    data = json.loads(response.text)
    comment_url = root_url + data['id']
    return comment_url