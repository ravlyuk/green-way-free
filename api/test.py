import requests
from lxml.html import fromstring

url = "https://www.forexfactory.com/calendar?day=today"

import httpx
resp = httpx.get("https://example.com").text

# resp = requests.get(url).text

page = fromstring(resp)

elems = page.xpath("//tr")

print(resp)
