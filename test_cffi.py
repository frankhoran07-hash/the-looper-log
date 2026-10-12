from curl_cffi import requests
from bs4 import BeautifulSoup

url = "https://www.boattrader.com/boats/make-mainship/"

# Impersonate a real Chrome browser session
response = requests.get(url, impersonate="chrome124")

print(f"Status Code: {response.status_code}")

if "Verify you are human" in response.text:
    print("Blocked by Cloudflare challenge.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    # Search for boat listing links or titles
    links = soup.find_all("a", href=lambda h: h and "/boat/" in h)
    print(f"Bypassed Cloudflare successfully. Found {len(links)} listing links.")