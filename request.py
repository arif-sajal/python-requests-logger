import requests as req
import logging
import re


class Request:

    def __init__(self):
        self.format = '<method> <url> json:<data> response_status_codee:<status_code>'  # Format String
        self.request = req.Session()  # Getting a requests session
        self.request.hooks["response"] = [self.log]  # Assigning the response Hook

    def log(self, response, *args, **kwargs):
        """
        This is the Actual place where logging is happening
        :param response:
        :param args:
        :param kwargs:
        :return None:
        """
        req = response.request

        # Preparing and formatting the json data for post request
        data = None
        if req.body is not None:
            if isinstance(req.body, bytes):
                data = req.body.decode('utf-8')  # Raw json Data

        # Assigning All attributes value for the format
        attrs = {
            "<method>": req.method,
            "<status_code>": response.status_code,
            "<url>": req.url,
            "<data>": data or {}
        }

        # Preparing the attributes
        params = dict((re.escape(k), str(v)) for k, v in attrs.items())
        pattern = re.compile("|".join(params.keys()))

        # Preparing the log format
        log_format = data is None and self.format.replace(' json:<data>', '') or self.format

        # Logging
        logging.info(pattern.sub(lambda m: params[re.escape(m.group(0))], log_format))

    def client(self):
        return self.request


def get_hooks():
    logger = Request().log
    return {'response': logger}


def get_client():
    return Request().client()


hooks = get_hooks()
requests = get_client()
