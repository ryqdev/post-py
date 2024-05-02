# system lib
import argparse
import json
import sys
from typing import NoReturn, Dict
import requests

# third-party lib
from loguru import logger

# local lib
from src.decorator import debug


# @debug
def run(endpoint: str, path: str, method: str, header: Dict[str, str], body: str) -> NoReturn:
    url = endpoint + path
    match method:
        case "GET":
            http_get(url)
        case "POST":
            http_post(url, header, body)
        case _:
            raise ValueError


def http_get(url: str) -> NoReturn:
    res = requests.get(url)
    logger.info(res.text)


def http_post(url: str, headers: Dict[str, str], body: str) -> NoReturn:
    res = requests.post(url, headers=headers, data=body)
    logger.info(f"response: {res.text}")


def parse_params(data: Dict[str, str]) -> (str, str, str, Dict[str, str], str):
    return (data["endpoint"] if data.get("endpoint") else "",
            data["path"] if data.get("path") else "",
            data["method"] if data.get("method") else "",
            data["headers"] if data.get("headers") else None,
            data["body"] if data.get("body") else "")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='mini client')
    parser.add_argument('--file',
                        type=str,
                        help='the local json file',
                        default='./config/get_example.json')

    args = parser.parse_args()
    file = args.file

    try:
        f = open(file)
        data = json.load(f)
    except IOError:
        logger.error("Fail to open json file")
        sys.exit(1)

    f.close()

    (endpoint, path, method, headers, body) = parse_params(data)

    run(endpoint, path, method, headers, json.dumps(body))
