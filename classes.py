import requests
from datetime import datetime, timedelta

class Predictor():
    def __init__(self):
        self.win = True
    
    def getTeams(self):
        return ['Bucks', 'Nuggets', 'Pelicans', 'Nets', 'Knicks', '76ers', 'Pacers', 'Cavaliers', 'Warriors', 'Jazz', 'Mavericks', 'Wizards', 'Hornets', 'Kings', 'Timberwolves', 'Grizzlies', 'Bulls', 'Raptors', 'Pistons', 'Rockets', 'Magic', 'Thunder', 'Clippers', 'Spurs', 'Heat', 'Lakers', 'Suns', 'Celtics', 'Trail Blazers', 'Hawks']
    

    def predict(self, team1, team2, betType):
        return "you winning big bucks fr!"


class Scraper():
    def __init__(self):
        self.url = "https://uswidgets.fn.sportradar.com/sportradarmlb/en_us/Etc:UTC/gismo/livescore_season_fixtures/119257"
        self.headers = {
            'Cookie': 'euConsent=true',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
        }
        self.date = datetime.now()

    def getUpcoming(self, periodDays):
        r = requests.get(url=self.url, headers=self.headers).json()
        matches = r['doc'][0]['data']['matches']
        upcoming = self.parseData(matches, periodDays) 
        return upcoming
    

    def parseData(self, matches, period):
        data = []
        for match in matches:
            if matches[match]['status']['name'] == "Not started":
                date = matches[match]['_dt']['date']
                if self.beforeDate(date, period):
                    home: str = matches[match]['teams']['home']['name']
                    away: str = matches[match]['teams']['away']['name']
                    home = home.split(" ")
                    away = away.split(" ")
                    i = 1 if home[0] == "LA" else 0 
                    j = 1 if away[0] == "LA" else 0

                    home = " ".join(home[i:])
                    away = " ".join(away[j:])

                    data.append({'home':home, 'away':away, 'date':date})
        
        return data
    

    def beforeDate(self, matchDate, period):
        formatDate = datetime.strptime(matchDate, "%m/%d/%Y")
        latestDate = self.date + timedelta(days=period)

        return formatDate < latestDate
    