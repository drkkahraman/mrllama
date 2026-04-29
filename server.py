#!/usr/bin/env python3
"""
Simple proxy server for MrLlama.
Serves static files AND proxies /api/* requests to Ollama,
so CORS is never an issue.
"""
import http.server
import urllib.request
import urllib.error
import os
import sys
import json

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            self._proxy("GET")
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/"):
            self._proxy("POST")
        else:
            self.send_error(405)

    def _proxy(self, method):
        url = OLLAMA_HOST + self.path
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else None

        req = urllib.request.Request(url, data=body, method=method)
        req.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))

        try:
            with urllib.request.urlopen(req) as resp:
                self.send_response(resp.status)
                # Forward content type
                ct = resp.headers.get("Content-Type", "application/json")
                self.send_header("Content-Type", ct)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                # Stream the response
                while True:
                    chunk = resp.read(4096)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    self.wfile.flush()
        except urllib.error.URLError as e:
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        # Cleaner logs
        sys.stderr.write(f"  {args[0]}\n")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(("0.0.0.0", PORT), ProxyHandler)
    print(f"\n  MrLlama Server running at http://127.0.0.1:{PORT}")
    print(f"  Proxying API to {OLLAMA_HOST}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
