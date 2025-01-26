from .utils import get_soup, get_base_url
import json
import re

base_url = get_base_url()


# Function to scrape the menu (Nav headers)
def scrape_menu():
    soup = get_soup()
    menu_data = []

    nav = soup.find_all("div", id="nav")
    for navs in nav:
        nav_headers = navs.find_all("div", class_="nav-header")
        for nav_header in nav_headers:
            menu_name = nav_header.get_text(strip=True)
            menu_data.append({"menu": menu_name})

    # json_data = json.dumps(menu_data, indent=4)
    return menu_data

# Function to scrape menu items based on selected menu
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

    # json_data = json.dumps(menu_item_data, indent=4)
    return menu_item_data


# Function to scrape category info
def scrape_category_info(category):
    soup = get_soup(category)
    category_data = {}

    category_info = soup.find("table", id="category-info")
    header_row = category_info.find("tr", class_="rowheader")
    rss_feed_url = header_row.find("a", href=True)["href"]
    category_data["rss_feed_url"] = f"{base_url}{rss_feed_url}"
    category_title = header_row.find("th").get_text(strip=True)
    category_data["category"] = category_title

    rows = category_info.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            data_title = cols[0].get_text(strip=True).lower().replace(" ", "_")
            data_value = cols[1].get_text(strip=True)
            category_data[data_title] = data_value

    # json_data = json.dumps(category_data, indent=4)
    return category_data


# Function to scrape category sections
def scrape_category_sections(category):
    soup = get_soup(category)
    sections = soup.find_all("div", class_="section")
    sections_data = []

    for section in sections:
        section_title = section.get_text(strip=True)
        items = []

        # Check if section title is "Recently Uploaded Sheets"
        # Also: if "Recently Uploaded Sheets" == section_title
        section_title_lower = section_title.lower()
        if "sheets" in section_title_lower:
            sheet_icons = section.find_next("div", class_="updatesheeticons").find_all(
                "a"
            )
            for sheet in sheet_icons:
                sheet_title = sheet.find("span", class_="iconheadertext")
                if sheet_title:
                    sheet_title = sheet_title.get_text(strip=True)
                    sheet_url = sheet.get("href")
                    sheet_image = sheet.find("img").get("src")

                    items.append(
                        {
                            "title": sheet_title,
                            "url": f"{base_url}{sheet_url}",
                            "image": f"{base_url}{sheet_image}",
                        }
                    )
        else:
            game_links = section.find_next("div").find_all("a")
            for game in game_links:
                game_title = game.find("span", class_="gameiconheadertext")
                if game_title:
                    game_title = game_title.get_text(strip=True)
                    game_url = game.get("href")
                    game_image = game.find("img").get("src")

                    items.append(
                        {
                            "title": game_title,
                            "url": f"{base_url}{game_url}",
                            "image": f"{base_url}{game_image}",
                        }
                    )

        sections_data.append({"section_title": section_title, "items": items})
        # json_data = json.dumps(data, indent=4)

    return sections_data


# Function to scrape category info & sections
def scrape_category_info_sections(category):
    soup = get_soup(category)
    sections = soup.find_all("div", class_="section")
    category_data = {}

    category_info = soup.find("table", id="category-info")
    header_row = category_info.find("tr", class_="rowheader")
    rss_feed_url = header_row.find("a", href=True)["href"]
    category_data["rss_feed_url"] = f"{base_url}{rss_feed_url}"
    category_title = header_row.find("th").get_text(strip=True)
    category_data["category"] = category_title

    rows = category_info.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            data_title = cols[0].get_text(strip=True).lower().replace(" ", "_")
            data_value = cols[1].get_text(strip=True)
            category_data[data_title] = data_value

    sections_data = []

    for section in sections:
        section_title = section.get_text(strip=True)
        items = []

        # Check if section title is "Recently Uploaded Sheets"
        # Also: if "Recently Uploaded Sheets" == section_title
        section_title_lower = section_title.lower()
        if "sheets" in section_title_lower:
            sheet_icons = section.find_next("div", class_="updatesheeticons").find_all(
                "a"
            )
            for sheet in sheet_icons:
                sheet_title = sheet.find("span", class_="iconheadertext")
                if sheet_title:
                    sheet_title = sheet_title.get_text(strip=True)
                    sheet_url = sheet.get("href")
                    sheet_image = sheet.find("img").get("src")

                    items.append(
                        {
                            "title": sheet_title,
                            "url": f"{base_url}{sheet_url}",
                            "image": f"{base_url}{sheet_image}",
                        }
                    )
        else:
            game_links = section.find_next("div").find_all("a")
            for game in game_links:
                game_title = game.find("span", class_="gameiconheadertext")
                if game_title:
                    game_title = game_title.get_text(strip=True)
                    game_url = game.get("href")
                    game_image = game.find("img").get("src")

                    items.append(
                        {
                            "title": game_title,
                            "url": f"{base_url}{game_url}",
                            "image": f"{base_url}{game_image}",
                        }
                    )

        sections_data.append({"section_title": section_title, "items": items})
        category_data["sections"] = sections_data
        # json_data = json.dumps(category_data, indent=4)

    return category_data


# Function to scrape search results and combine data
def scrape_search_results(keyword):
    soup = get_soup(f"/search/?q={keyword}")
    search_results_data = {}

    sections = soup.find_all("div", class_="section")

    for section in sections:
        section_title = section.get_text(strip=True)
        section_count = int(re.findall(r"\((\d+)\)", section_title.replace(",", ""))[0])

        section_title_lower = section_title.lower()
        if "sheet results" in section_title_lower:
            category = "sheet_results"
        elif "game results" in section_title_lower:
            category = "game_results"
        else:
            continue

        if category not in search_results_data:
            search_results_data[category] = {
                "title": section_title,
                "count": section_count,
                "items": [],
            }

        icons = section.find_next(
            "div", class_="updatesheeticons"
        ) or section.find_next("div", style="text-align: center; margin-top: 10px;")

        if icons:
            for idx, icon in enumerate(icons.find_all("a", href=True), 1):
                item_data = {
                    "id": idx,
                    "title": icon.find("span").get_text(strip=True),
                    "link": f'{base_url}{icon["href"]}',
                    "image_url": f'{base_url}{icon.find("img")["src"]}',
                }
                search_results_data[category]["items"].append(item_data)

    # json_data = json.dumps(search_results_data, indent=4)
    return search_results_data
