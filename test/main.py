from bs4 import BeautifulSoup
import requests

url = 'https://www.spriters-resource.com/mobile/touhoulostword/'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

sections = soup.find_all('div', class_='section')

for section in sections:
    title = section.find('div', class_='sect-name').get_text(strip=True)
    count = section.find('span', class_='sect-count').get_text(strip=True)

    print(f"Section Title: {title}")
    print(f"Section Count: {count}")
    
    contents = section.find_next('div', class_='updatesheeticons')

    if contents:
        for content in contents.find_all('a'):
            link = content['href']
            
            img_url = content.find('img')['src'] if content.find('img') else None
            
            icon_title = content.find('span', class_='iconheadertext').text.strip() if content.find('span', class_='iconheadertext') else None

            print(f"  Title: {icon_title}")
            print(f"  Link: {link}")
            print(f"  Image URL: {img_url}")
    else:
        print("  No contents found in this section.")
    
    print('---')
