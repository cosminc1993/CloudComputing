#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
from RequestProcessor import RequestProcessor


class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n",
                     str(self.path), str(self.headers))

        processor_of_requests = RequestProcessor()
        response, content_response = processor_of_requests.process_get_path(
            self.path)

        if response == True:
            self.send_response(200)

        self.wfile.write(json.dumps(content_response).encode())

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        processor_of_requests = RequestProcessor()
        add_phones_respone = processor_of_requests.process_add_phones(
            self.path, post_data)

        if add_phones_respone == True:
            response_msg = "Adding a phone was successfully"
            self.send_response(200)
        else:
            self.send_error(
                404, 'The correct path to add a phone is /add/phones')
            return

        self.wfile.write(response_msg.encode('utf-8'))


def run():
    logging.basicConfig(level=logging.INFO)
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    run()
