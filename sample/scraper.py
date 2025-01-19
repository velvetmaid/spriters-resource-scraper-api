from bs4 import BeautifulSoup
import toml
import requests
import json


def scrape_touhou():
    config = toml.load('.toml')
    base_url = config['settings']['base_url']
    url = f"{base_url}/mobile/touhoulostword/"

    response = requests.get(url)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    sections = soup.find_all("div", class_="section")
    for section in sections:
        title = section.find("div", class_="sect-name").get_text(strip=True)
        count = section.find("span", class_="sect-count").get_text(strip=True)

        section_data = {"section_title": title, "section_count": count, "contents": []}
        contents = section.find_next("div", class_="updatesheeticons")
        for content in contents.find_all("a", href=True):
            link = base_url + content["href"]
            img_url = base_url + content.find("img")["src"]
            icon_title = content.find("span", class_="iconheadertext").text.strip()

            section_data["contents"].append(
                {"title": icon_title, "link": link, "image_url": img_url}
            )
        data.append(section_data)

    return json.dumps(data, indent=4)


result = scrape_touhou()
print(result)
