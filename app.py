from flask import Flask, render_template, request
from classes import Predictor, Scraper 

app = Flask(__name__)

predictor = Predictor()
scraper = Scraper()

@app.route("/")
def main():
    teams = predictor.get_teams()
    upcomingGames = scraper.getUpcoming(3)
    return render_template("frontend.html", teams = teams, upcomingGames = upcomingGames)

@app.route("/predict", methods=["POST"])
def prediction():
    
    team1 = request.form.get("team1")
    team2 = request.form.get("team2")
    bet = request.form.get("bet")

    if not all([team1, team2, bet]):
        return {"error": "All fields are required!"}, 400

    if team1 == team2:
        return {"error": "Team 1 and Team 2 cannot be the same!"}, 400

    prediction = predictor.predict_scores(team1, team2, bet)

    return render_template("results.html", prediction = prediction)#, 200


if __name__ == "__main__":
    app.run(debug=True)
