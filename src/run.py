# system lib
import argparse
import json
from typing import NoReturn, Dict
import requests

# third-party lib
from loguru import logger

# local lib
from decorator import debug


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tttest')
    parser.add_argument('--method',
                        type=str,
                        help='the http method type (get | post)',
                        choices=["get", "post"],
                        default='get')

    args = parser.parse_args()

    endpoint = "https://you-search-zeta.vercel.app"
    path = "/ping"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "id": "hello"
    }
    run(endpoint, path, "POST", headers, json.dumps(body))
