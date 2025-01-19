from .utils import get_soup
import json


def scrape_menu():
    soup = get_soup()
    menu_data = []

    nav = soup.find_all("div", id="nav")

    for navs in nav:
        nav_headers = navs.find_all("div", class_="nav-header")
        for nav_header in nav_headers:
            menu_name = nav_header.get_text(strip=True)
            menu_data.append({"menu": menu_name})

    json_data = json.dumps(menu_data, indent=4)
    return json_data


def scrape_menu_item(selected_menu):
    soup = get_soup()
    selected_menu = selected_menu.lower()
    menu_item_data = []

    leftnav = soup.find("div", id=f"leftnav-{selected_menu}")

    if leftnav:
        links = leftnav.find_all("a", href=True)
        for link in links:
            leftnav_link = link["href"]
            leftnav_title = link.get_text(strip=True)
            menu_item_data.append({"title": leftnav_title, "link": leftnav_link})

    json_data = json.dumps(menu_item_data, indent=4)
    return json_data


result = scrape_menu_item("cOnsolES")
print(result)
