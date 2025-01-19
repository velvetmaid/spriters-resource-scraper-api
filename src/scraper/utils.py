from bs4 import BeautifulSoup
import toml
import requests


def get_soup(path=""):
    config = toml.load(".toml")
    base_url = config["settings"]["base_url"]
    url = f"{base_url}/{path}"

    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")
