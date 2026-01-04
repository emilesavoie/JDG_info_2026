# This is an example HTTP server that returns a response
import http.server
import urllib.parse

PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if path == "/drink-ingredients":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"drink-ingredients": ["gin", "tequila", "vodka"]}')
        elif path == "/drink":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if "type" in params and params["type"][0] == "gin":
                self.wfile.write(b'{"drink": "gin-tonic"}')
            else:
                self.wfile.write(b'{"drink": "tequila-sunrise"}')

        elif path == "/meal-ingredients":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"meal-ingredients": ["chicken", "beef", "veal"]}')
        elif path == "/meals":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if "type" in params and params["type"][0] == "chicken":
                self.wfile.write(b'{"meal": "chicken-salad"}')
            else:
                self.wfile.write(b'{"meals": "beef-stroganoff"}')

        elif path == "/game-types":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"game-types": ["shooter", "puzzle", "strategy"]}')
        elif path == "/game":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if "type" in params and params["type"][0] == "shooter":
                self.wfile.write(b'{"game": "call-of-duty"}')
            else:
                self.wfile.write(b'{"game": "the-sims"}')

        elif path == "/music-genres":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"music-genres": ["rock", "pop", "jazz", "classical", "hip-hop"]}')
        elif path == "/music":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if "genre" in params and params["genre"][0] == "rock":
                self.wfile.write(b'{"music": ["rock-song1", "rock-song2", "rock-song3", "rock-song4", "rock-song5"]}')
            else:
                self.wfile.write(b'{"music": ["pop-song1", "alternative-song2", "metal-song3", "jazz-song4", "blues-song5"]}')

httpd = http.server.HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)
print(f"Serving on port {PORT}")
httpd.serve_forever()
