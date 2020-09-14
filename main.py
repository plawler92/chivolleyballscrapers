import logging

import requests
from bs4 import BeautifulSoup
from collections import namedtuple

Schedule = namedtuple("Schedule", "league, day, gender, skill, format, time, start_date, team_price, solo_price, location")

def get_css_schedule(url, refresh=False):
    url = "https://chicagosocial.com/sports/indoor-volleyball/"
    r = requests.get(url)
    with open("css-vb.html", "wb") as f:
        f.write(r.content)

def parse_css(content):
    schedules = []
    league = "Chicago Sports and Social"
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.select(".hide-on-mobile.league-row")
    for row in rows:
        try:
            cols = row.select("td")
            day = cols[1].text.strip()
            location = cols[2].text.strip()
            gender = cols[3].text.strip()
            skill = cols[4].text.strip()
            fmt = cols[5].text.strip()
            time = cols[6].text.strip()
            start_date = cols[7].text.strip()
            team_price = cols[8].text.strip()
            solo_price = cols[9].text.strip()
            schedules.append(Schedule(league, day, gender, skill, fmt, time, start_date, team_price, solo_price, location))
        except Exception as e:
            logging.error(str(e))
    return schedules

with open("css-vb.html", "rb") as f:
    content = f.read()
    s = parse_css(content)
    for sch in s:
        print(sch)