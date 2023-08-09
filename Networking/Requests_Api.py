import json

import requests

CATS_API_SEVER_URL: str = "https://catfact.ninja/"


def get_cat_fact():
    response = requests.get(CATS_API_SEVER_URL + "fact")
    print(response.text)


if __name__ == '__main__':
    get_cat_fact()
