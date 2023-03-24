import requests
import logging
import re


class Request:

    def __init__(self):
        self.format = '<method> <url> json:<data> response_status_codee:<status_code>'
        self.request = requests.Session()
        self.request.hooks["response"] = [self.log]

    def log(self, response, *args, **kwargs):
        req = response.request

        data = None
        if req.body is not None:
            if isinstance(req.body, bytes):
                data = req.body.decode('utf-8')
            elif isinstance(req.body, str):
                data = dict(x.split("=", -1) for x in req.body.split("&", -1))

        attrs = {
            "<method>": req.method,
            "<status_code>": response.status_code,
            "<url>": req.url,
            "<data>": data or {}
        }

        params = dict((re.escape(k), str(v)) for k, v in attrs.items())
        pattern = re.compile("|".join(params.keys()))

        log_format = data is None and self.format.replace(' json:<data>', '') or self.format
        logging.info(pattern.sub(lambda m: params[re.escape(m.group(0))], log_format))

    def client(self):
        return self.request
