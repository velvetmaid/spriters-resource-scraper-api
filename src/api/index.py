from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from src.scraper.scraper import *
import json


class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        try:
            if path == "/":
                response = {"status": "success", "success": True}
            elif path == "/menus":
                data = scrape_menu()
                response = {"status": "success", "success": True, "data": data}
            elif path.startswith("/menu_items/"):
                item = path.split("/")[-1]
                data = scrape_menu_item(item)
                response = {
                    "status": "success",
                    "success": True,
                    "param": item,
                    "data": data,
                }
            elif path.startswith("/category_info/"):
                category = path.split("/")[-1]
                data = scrape_category_info(category)
                response = {
                    "status": "success",
                    "success": True,
                    "param": category,
                    "data": data,
                }
            elif path.startswith("/category_sections/"):
                category = path.split("/")[-1]
                data = scrape_category_sections(category)
                response = {
                    "status": "success",
                    "success": True,
                    "param": category,
                    "data": data,
                }
            elif path.startswith("/category_info_sections/"):
                category = path.split("/")[-1]
                data = scrape_category_info_sections(category)
                response = {
                    "status": "success",
                    "success": True,
                    "param": category,
                    "data": data,
                }
            elif path.startswith("/search/"):
                keyword = path.split("/")[-1]
                data = scrape_search_results(keyword)
                response = {
                    "status": "success",
                    "success": True,
                    "keyword": keyword,
                    "data": data,
                }
            else:
                self._set_headers(404)
                response = {"status": "error", "success": False, "message": "Not Found"}
                self.wfile.write(json.dumps(response).encode())
                return
            self._set_headers(200)
        except Exception as e:
            self._set_headers(500)
            response = {"status": "error", "success": False, "message": str(e)}
        self.wfile.write(json.dumps(response).encode())


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is stopping...")
    finally:
        httpd.server_close()
        print("Server stopped.")


if __name__ == "__main__":
    run()
