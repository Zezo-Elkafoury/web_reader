from bs4 import BeautifulSoup

def extract_content(soup: BeautifulSoup):
    content = {
        "buttons": [],
        "texts": [text.get_text(strip=True) for text in soup.find_all(['p', 'span', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
        "inputs": [],
        "navbars": [],
        "images": [],
        "footers": []
    }

    for button in soup.find_all(['button', 'a']):
        if button.get('role') == 'button' or button.name == 'button':
            button_content = {
                "text": button.get_text(strip=True),
                "x": button.get('x', 'N/A'),
                "y": button.get('y', 'N/A')
            }
            content["buttons"].append(button_content)

    for navbar in soup.find_all('nav'):
        navbar_content = {
            "text": navbar.get_text(strip=True),
            "x": navbar.get('x', 'N/A'),
            "y": navbar.get('y', 'N/A')
        }
        content["navbars"].append(navbar_content)

    for img in soup.find_all('img'):
        img_content = {
            "src": img.get('src'),
            "x": img.get('x', 'N/A'),
            "y": img.get('y', 'N/A')
        }
        content["images"].append(img_content)

    for footer in soup.find_all('footer'):
        footer_content = {
            "text": footer.get_text(strip=True),
            "x": footer.get('x', 'N/A'),
            "y": footer.get('y', 'N/A')
        }
        content["footers"].append(footer_content)

    for input_tag in soup.find_all('input'):
        input_content = {
            "type": input_tag.get('type'),
            "name": input_tag.get('name'),
            "value": input_tag.get('value'),
            "placeholder": input_tag.get('placeholder'),
            "x": input_tag.get('x', 'N/A'),
            "y": input_tag.get('y', 'N/A')
        }
        content["inputs"].append(input_content)

    return content