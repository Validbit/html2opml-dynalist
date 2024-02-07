import html #escaúing quotes/symbols
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def convert_html_to_opml(html_content):
    soup = BeautifulSoup(html_content, 'lxml')

    def parse_element(element):
        opml_outline = ''

        if element.name == 'h3':  # folder
            opml_outline += f'<outline text="{html.escape(element.get_text(strip=True))}">'
            dl = element.find_next('dl')
            if dl:
                for dt in dl.find_all('dt', recursive=False):  # only get direct children
                    opml_outline += parse_element(dt)
            opml_outline += '</outline>'
        elif element.name == 'a':  # bookmark
            opml_outline += f'<outline text="{html.escape(element.get_text(strip=True))}" _note="{html.escape(element["href"])}"/>'
        elif element.name == 'dt':  # dt containing a or h3
            for child in element.contents:  # only get direct children
                opml_outline += parse_element(child)

        return opml_outline

    opml_content = ''
    for dt in soup.dl.find_all('dt', recursive=False):  # only get top-level elements
        opml_content += parse_element(dt)
    opml_content = f'{opml_header_inline}{opml_content}</body></opml>'
    return opml_content

# FILL HERE ------------------------------------------

# HTML bookmarks content (chrome)
html_content = """

"""
# Dynalist header (replace with your own)
opml_header_inline = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><opml version="2.0"><head><title>Your Bookmarks</title><flavor>dynalist</flavor><source>https://dynalist.io</source><ownerName>FirstLast</ownerName><ownerEmail>you@example.com</ownerEmail></head><body>"""

# ----------------------------------------------------

opml_result = convert_html_to_opml(html_content)
# print(opml_result)
with open('output_dyna.opml', 'w', encoding='utf-8') as f:
    f.write(opml_result)
