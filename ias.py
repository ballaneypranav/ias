import requests
from bs4 import BeautifulSoup
import discord_notify as dn
import os

s = requests.Session()
API_url = 'https://webjapps.ias.ac.in/fellowship2021/lists/selectedList.jsp'

request_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36",
    "Referer": "https://webjapps.ias.ac.in/fellowship2021/lists/result.jsp",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "JSESSIONID=DEEED769CD07BB27DCD68B6EF4459E51"
}

params = {'subject': 'Lif'}

r = s.get(API_url, params=params, headers=request_headers)
soup = BeautifulSoup(r.content, 'html5lib')

DISCORD_URL = os.environ.get('DISCORD_URL')
print(DISCORD_URL)
notifier = dn.Notifier(DISCORD_URL)

if "Ballaney, Mr Pranav" in str(soup):
    notifier.send("Yayyyy!", print_message=False)

notifier.send("Yayyyy!", print_message=False)