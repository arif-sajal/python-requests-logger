from request import Request
import logging

logging.basicConfig(format='INFO: %(message)s')
logging.root.setLevel(logging.INFO)

req = Request().client()

req.get("https://jsonplaceholder.typicode.com/posts")

req.post("https://jsonplaceholder.typicode.com/posts")
req.post("https://jsonplaceholder.typicode.com/posts", json={})
req.post("https://jsonplaceholder.typicode.com/posts", json={"country": "BD", "state": "Dhaka"})

req.patch("https://jsonplaceholder.typicode.com/posts/1")
req.patch("https://jsonplaceholder.typicode.com/posts/1", json={})
req.patch("https://jsonplaceholder.typicode.com/posts/1", json={"country": "BD", "state": "Dhaka"})
