from request import Request, get_hooks
import requests
import logging

# Formatting the python logger
logging.basicConfig(format='INFO: %(message)s')
logging.root.setLevel(logging.INFO)

# Initiating requests client
req = Request().client()

# Request tests
req.get("https://jsonplaceholder.typicode.com/posts")
requests.get("https://jsonplaceholder.typicode.com/posts", hooks=get_hooks())

req.post("https://jsonplaceholder.typicode.com/posts")
requests.post("https://jsonplaceholder.typicode.com/posts", hooks=get_hooks())

req.post("https://jsonplaceholder.typicode.com/posts", json={})
requests.post("https://jsonplaceholder.typicode.com/posts", json={}, hooks=get_hooks())

req.post("https://jsonplaceholder.typicode.com/posts", json={"country": "BD", "state": "Dhaka"})
requests.post("https://jsonplaceholder.typicode.com/posts", json={"country": "BD", "state": "Dhaka"}, hooks=get_hooks())

req.patch("https://jsonplaceholder.typicode.com/posts/1")
requests.patch("https://jsonplaceholder.typicode.com/posts", hooks=get_hooks())

req.patch("https://jsonplaceholder.typicode.com/posts/1", json={})
requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={}, hooks=get_hooks())

req.patch("https://jsonplaceholder.typicode.com/posts/1", json={"country": "BD", "state": "Dhaka"})
requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={"country": "BD", "state": "Dhaka"}, hooks=get_hooks())
