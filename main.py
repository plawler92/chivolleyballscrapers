import logging

import requests
from bs4 import BeautifulSoup

css_url = "https://chicagosocial.com/sports/indoor-volleyball/"

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
            schedules.append({
                'day': day,
                'location': location,
                'gender': gender,
                'skill': skill,
                'fmt': fmt,
                'time': time,
                'start_date': start_date,
                'team_price': team_price,
                'solo_price': solo_price
            })
        except Exception as e:
            logging.error(str(e))
    return schedules

url = "https://chicagosocial.com/sports/indoor-volleyball/"
r = requests.get(url)
s = parse_css(r.content)
for sch in s:
    print(sch)
