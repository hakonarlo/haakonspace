#!/usr/bin/env python3
"""
Minimal dashboard server.
- Serves all static files (dashboard.html, etc.) exactly like python3 -m http.server
- Adds one extra route: GET /api/news  →  fetches NRK RSS server-side and returns JSON
"""
import http.server
import urllib.request
import json
import xml.etree.ElementTree as ET
import os

PORT = 8080


class Handler(http.server.SimpleHTTPRequestHandler):

    def log_message(self, fmt, *args):
        pass  # keep the terminal quiet

    def do_GET(self):
        if self.path == '/api/news':
            self._serve_news()
        else:
            super().do_GET()  # static files handled normally

    def _serve_news(self):
        try:
            req = urllib.request.Request(
                'https://www.nrk.no/nyheter/siste.rss',
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=10) as r:
                root = ET.fromstring(r.read())

            items = root.findall('.//item')[:3]
            news = [
                {
                    'title':   i.findtext('title',   '').strip(),
                    'link':    i.findtext('link',    '').strip(),
                    'pubDate': i.findtext('pubDate', '').strip(),
                }
                for i in items
            ]
            self._json(news)

        except Exception as e:
            self._json({'error': str(e)}, 500)

    def _json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    httpd = http.server.HTTPServer(('localhost', PORT), Handler)
    print(f'\n  Dashboard → http://localhost:{PORT}/dashboard.html')
    print('  Press Ctrl+C to stop.\n')
    httpd.serve_forever()
