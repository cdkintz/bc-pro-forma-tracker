import http.server
import json
import os

PORT = 8899
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == "/save":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                formatted = json.dumps(data, indent=2, ensure_ascii=False)
                filepath = os.path.join(DIRECTORY, "data.json")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(formatted + "\n")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    print(f"Serving at http://localhost:{PORT}")
    print(f"Saving to {os.path.join(DIRECTORY, 'data.json')}")
    server = http.server.HTTPServer(("", PORT), Handler)
    server.serve_forever()
