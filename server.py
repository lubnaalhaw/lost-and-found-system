
import sqlite3
import json
import os

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")


class MyHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):

        path = urlparse(self.path).path

        if path == "/api/items":

            db = sqlite3.connect(DB_PATH)
            db.row_factory = sqlite3.Row
            c = db.cursor()

            c.execute("""
                SELECT id, item_name, category, item_date,
                       status, description, location
                FROM items
                ORDER BY id DESC
            """)

            items = [dict(row) for row in c.fetchall()]

            db.close()

            response = json.dumps(items).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()

            self.wfile.write(response)

        else:
            super().do_GET()


server = HTTPServer(("127.0.0.1", 8000), MyHandler)

print("Server is running at http://localhost:8000")

server.serve_forever()
