from flask import Flask, render_template, request, redirect, url_for
from predict import Redo 
app = Flask(__name__)

predictor = Redo()
@app.route("/")
def main():
    teams = predictor.getTeams()
    return render_template("frontend.html", teams = teams)

@app.route("/predict", methods=["POST"])
def prediction():
    team1 = request.form.get("team1")
    team2 = request.form.get("team2")
    sport = request.form.get("sport")
    bet = request.form.get("bet")
    if not all([team1, team2, sport, bet]):
        return {"error": "All fields are required!"}, 400

    if team1 == team2:
        return {"error": "Team 1 and Team 2 cannot be the same!"}, 400

    prediction = predictor.predict(sport = sport, team1=team1, team2=team2, betType=bet)

    return {"prediction": prediction}, 200


if __name__ == "__main__":
    app.run(debug=True)
