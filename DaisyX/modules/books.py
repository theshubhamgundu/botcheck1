#Collabration with Friday Project
import requests
import os
import re
import sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from EMAA.services.telethon import tbot
from telethon import events


@tbot.on(events.NewMessage(pattern="^/book (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lool = 0
    KkK = await event.reply( "searching for the book...")
    lin = "https://b-ok.cc/s/"
    text = input_str
    link = lin+text

    headers = ['User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0']
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    f = open("book.txt",'w')
    total = soup.find(class_="totalCounter")
    for nb in total.descendants:
      nbx = nb.replace("(", "").replace(")", "")
    if nbx == "0":
        await event.reply( "No Books Found with that name.")
    else:

        for tr in soup.find_all('td'):
            for td in tr.find_all('h3'):
                for ts in td.find_all('a'):
                    title = ts.get_text()
                    lool = lool+1
                for ts in td.find_all('a', attrs={'href': re.compile("^/book/")}):
                    ref = (ts.get('href'))
                    link = "https://b-ok.cc" + ref

                f.write("\n"+title)
                f.write("\nBook link:- " + link+"\n\n")

        f.write("BY @EmmaAGroup_bot.")
        f.close()
        caption="A collabration with Friday.\n Join Support @Emaabot_support"
        
        await tbot.send_file(event.chat_id, "book.txt", caption=f"**BOOKS GATHERED SUCCESSFULLY!\n\nBY DAISYX. JOIN THE SUPPORT @DaisySupport_Official.**")
        os.remove("book.txt")
        await KkK.delete()
        

