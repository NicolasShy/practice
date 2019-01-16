

def app(environ, start_response):
    start_response("200 OK", [("Content-Type","text/html")])
    return ["Hello world!\n"]

from wsgiref.simple_server import make_server

if __name__ == "__main__":
    httpd = make_server("", 8000, app)
    print("Serving http on port 8000")
    httpd.serve_forever()