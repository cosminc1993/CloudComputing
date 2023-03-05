from urllib.parse import urlparse

import logging
from ConnectDB import MongoDB
from urllib.parse import urlparse, parse_qs
import json


class RequestProcessor():
    def __init__(self) -> None:
        self.db = MongoDB()

    def extract_path_and_params(self, path):
        query_parameters = parse_qs(urlparse(path).query)
        params_of_query = {}
        for key, value in query_parameters.items():
            params_of_query[key] = value[0]
        only_path = urlparse(path).path
        return params_of_query, only_path

    def process_add_phones(self, path, request_data):
        params_of_query, only_path = self.extract_path_and_params(path)
        is_model_found, model_found = self.db.check_add_valid_path(only_path)
        if is_model_found == True:
            if len(request_data) > 0:
                model_to_be_aded = {model_found: request_data}
                return self.db.insert_data(model_to_be_aded)
            return self.db.insert_data(request_data)
        else:
            return False

    def process_get_path(self, path):
        logging.info("path is " + path)

        params_of_query, only_path = self.extract_path_and_params(path)

        path_splitted = only_path.split("/")
        if path_splitted[1] == "all":
            response = self.extract_data_from_db(self)
        return True, response

        # self.db.insert_data(data)

        # query_components = dict(qc.split("=") for qc in query.split("&"))
        # A GET request to the API
        # response = requests.get(path)

        # Print the response
        # response_json = response.json()
        # print(response_json)

    def extract_data_from_db(self, query: "{}"):
        response = self.db.get_all_data()
        logging.info("yes")
        return response
