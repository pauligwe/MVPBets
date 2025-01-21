import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



class Predictor:
    def __init__(self):
        self.df = pd.read_csv("games.csv")
        self.names = self.get_teams()
        self.names_dict_points = self.points()
        self.df = self.update_winner_column()
        
    def get_teams(self):
        return list(set(self.df["hometeamName"]))
    
    def points(self):
        names_dict_points = {name: [] for name in self.names}
        for i, row in self.df.iterrows():
            names_dict_points[row["hometeamName"]].append(row["homeScore"])
            names_dict_points[row["awayteamName"]].append(row["awayScore"])
        return names_dict_points
    
    def linear_regression(self, team_name):
        team_points = self.names_dict_points.get(team_name, [])
        team_games = list(range(len(team_points)))
        team_model = LinearRegression()
        team_model.fit(np.array(team_games).reshape(-1, 1), np.array(team_points).reshape(-1, 1))
        team_predictions = team_model.predict(np.array(team_games).reshape(-1, 1))
        team_next_game = len(team_points)
        team_next_prediction = team_model.predict([[team_next_game]])
        return team_games, team_points, team_predictions, team_next_prediction

    def update_winner_column(self):
        self.df["Diff"] = self.df["homeScore"] - self.df["awayScore"]
        self.df["Winner"] = self.df.apply(
            lambda row: row["hometeamName"] if row["Diff"] > 0 else (row["awayteamName"] if row["Diff"] < 0 else "Tie"), axis=1
        )
        return self.df
    
    def predict_scores(self, team1_name, team2_name, type):
        team1_next_prediction = round(self.linear_regression(team1_name)[3][0][0])
        team2_next_prediction = round(self.linear_regression(team2_name)[3][0][0])

        game = {
            "team1" : team1_name,
            "team2" : team2_name,
            "score1": round(team1_next_prediction), 
            "score2":round(team2_next_prediction)
            }
        

        game["total"] = team1_next_prediction + team2_next_prediction


        if team1_next_prediction > team2_next_prediction:
            game["winner"] = team1_name
            
        elif team1_next_prediction == team2_next_prediction:
            game["winner"] = "TIE"
        else:
            game["winner"] = team2_name

        return game
        
        return {"error":"Select a Valid Bet Type"}

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
    
    