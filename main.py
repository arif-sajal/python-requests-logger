from request import Request, hooks, requests
# import requests
import logging

# Formatting the python logger
logging.basicConfig(format='INFO: %(message)s')
logging.root.setLevel(logging.INFO)

# Initiating requests client
req = Request().client()

# Request tests
req.get("https://jsonplaceholder.typicode.com/posts")
requests.get("https://jsonplaceholder.typicode.com/posts")
#requests.get("https://jsonplaceholder.typicode.com/posts", hooks=hooks)

req.post("https://jsonplaceholder.typicode.com/posts")
requests.post("https://jsonplaceholder.typicode.com/posts")
#requests.post("https://jsonplaceholder.typicode.com/posts", hooks=hooks)

req.post("https://jsonplaceholder.typicode.com/posts", json={})
requests.post("https://jsonplaceholder.typicode.com/posts", json={})
#requests.post("https://jsonplaceholder.typicode.com/posts", json={}, hooks=hooks)

req.post("https://jsonplaceholder.typicode.com/posts", json={"country": "BD", "state": "Dhaka"})
requests.post("https://jsonplaceholder.typicode.com/posts", json={"country": "BD", "state": "Dhaka"})
#requests.post("https://jsonplaceholder.typicode.com/posts", json={"country": "BD", "state": "Dhaka"}, hooks=hooks)

req.patch("https://jsonplaceholder.typicode.com/posts/1")
requests.patch("https://jsonplaceholder.typicode.com/posts")
#requests.patch("https://jsonplaceholder.typicode.com/posts", hooks=hooks)

req.patch("https://jsonplaceholder.typicode.com/posts/1", json={})
requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={})
#requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={}, hooks=hooks)

req.patch("https://jsonplaceholder.typicode.com/posts/1", json={"country": "BD", "state": "Dhaka"})
requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={"country": "BD", "state": "Dhaka"})
#requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={"country": "BD", "state": "Dhaka"}, hooks=hooks)
