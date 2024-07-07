# Titanic Survival Prediction

This project predicts the survival of passengers on the Titanic using a Logistic Regression model. The prediction is made through a Flask web application where users can input passenger details and receive a prediction.

## Project Structure

titanic_survival_prediction/
│
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── styles.css
├── logistic_regression_model.pkl
├── README.md
└── requirements.txt

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `static/styles.css`: The CSS file for styling the web interface.
- `logistic_regression_model.pkl`: The pre-trained Logistic Regression model.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.


#Run the Flask application:

##python app.py

##Open a web browser and go to http://127.0.0.1:5000/.


#Usage
##Fill in the form with the following passenger details:

Passenger Class (1/2/3)
Sex (0 for male, 1 for female)
Age
Siblings/Spouses Aboard
Parents/Children Aboard
Fare
Embarked (0 for S, 1 for C, 2 for Q)
#Click "Predict" to see whether the passenger survived or not.

##Examples
##Survival Input
Passenger Class: 1
Sex: 1 (Female)
Age: 29
Siblings/Spouses Aboard: 0
Parents/Children Aboard: 0
Fare: 100.0
Embarked: 1 (Cherbourg)
##Non-Survival Input
Passenger Class: 3
Sex: 0 (Male)
Age: 35
Siblings/Spouses Aboard: 1
Parents/Children Aboard: 0
Fare: 8.05
Embarked: 0 (Southampton)
