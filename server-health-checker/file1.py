import json
import logging
import argparse

logging.basicConfig(level=logging.INFO) # To print info message because error will be print by default.

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()







def load_servers(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        logging.error(f"{filename} file not found")
        return None


def check_servers(data):
    if data is None: #This handle if json file not found.
        return

    for server in data:
        if server["cpu"] > 80:
            logging.error(f"high cpu on {server['name']}")
        else:
            logging.info(f"{server['name']} is healthy")

data = load_servers(args.file)
check_servers(data)


