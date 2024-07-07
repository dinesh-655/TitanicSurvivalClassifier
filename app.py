from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the logistic regression model
try:
    with open('logistic_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text='Model not loaded correctly.')
    
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction =model.predict(final_features)
        output = 'Survived' if prediction[0] == 1 else 'Not Survived'
        return render_template('index.html', prediction_text='Prediction: {}'.format(output))
    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('index.html', prediction_text='Error during prediction.')

if __name__ == "__main__":
    app.run(debug=True)
