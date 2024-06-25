from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import Final

DIRECTORY: Final[str] = "templates"

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Last-Modified", "")
        return super(CORSRequestHandler, self).end_headers()


httpd = HTTPServer(("localhost", 8003), CORSRequestHandler)
print("Running local server exposing port 8003 for template builder")


httpd.serve_forever()
