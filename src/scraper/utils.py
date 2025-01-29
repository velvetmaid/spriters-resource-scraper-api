from fastapi import HTTPException
from bs4 import BeautifulSoup
import toml
import requests

config = toml.load(".toml")
base_url = config["settings"]["base_url"]


def get_base_url():
    return base_url


def get_soup(path=""):
    url = f"{base_url}/{path}"

    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def check_base_url():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            return {
                "status": "success",
                "message": f"URL {base_url} is valid and reachable.",
            }
        else:
            raise HTTPException(
                status_code=400,
                detail=f"URL {base_url} returned status code {response.status_code}",
            )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
