# MVPBets - NBA Score Predictor 🏀  

## Overview  
MVPBets is a web application that predicts NBA game scores using **machine learning**. It utilizes **linear regression** to forecast scores based on historical game data and fetches **real-time sports data** through web scraping.  

## Features  
- **NBA Score Prediction** using a trained linear regression model.  
- **Live Data Scraping** to fetch upcoming game schedules.  
- **Flask Backend** for handling API requests and rendering predictions.  
- **Automated Winner Calculation** based on predicted scores.  

## Tech Stack  
- **Backend:** Flask, Python  
- **Machine Learning:** scikit-learn (Linear Regression), pandas, NumPy  
- **Web Scraping:** Requests  
- **Frontend:** HTML, CSS, JavaScript  

## Installation & Setup  
### Prerequisites  
- Python 3.8+  
- pip (Python package manager)  
- Virtual environment (optional)  

### Installation Steps  
1. **Clone the repository**  
   git clone https://github.com/yourusername/mvpbets.git

2. **Create and activate a virtual environment (optional)**  
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**  
   pip install -r requirements.txt

4. **Run the Flask app**  
   python app.py

5. **Open the application in your browser**  
   http://127.0.0.1:5000

## ⚙️ How It Works  
📥 1. **Data Collection**  
   - Loads historical NBA game data from `games.csv`.  
   - Fetches upcoming game schedules in real-time from a sports API.  

🤖 2. **Score Prediction Model**  
   - Built using linear regression from scikit-learn.  
   - Analyzes past game data to predict future scores.  
   - Predictions are displayed with upcoming game schedules.  

🌐 3. **Web Scraping**  
   - Uses the Requests library to fetch live NBA game data.  
   - Extracts team names and game dates for the frontend.  

🔥 4. **Flask Backend**  
   - Handles team selection and score prediction requests.  
   - Processes API responses and sends predicted scores to the frontend.  

🎮 **Usage**  
1️⃣ Select two NBA teams from the dropdown.  
2️⃣ Choose a bet type (e.g., MoneyLine, Over/Under).  
3️⃣ Submit to receive the predicted score and winner.

🚀 **Future Improvements**  
- Expand dataset for better model accuracy.  
- Experiment with additional machine learning models (e.g., decision trees, neural networks).  
- Integrate additional betting options.  
- Enhance UI/UX for a better user experience.  

🤝 **Contributing**  
Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new feature branch.  
3. Commit your changes.  
4. Submit a pull request.

📜 **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
