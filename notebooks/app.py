from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

class Model:
    def __init__(self):
        self.model = None
        self.load_model('notebooks/eda_model.pkl')


    def load_model(self, model_name):
        self.model = joblib.load(model_name)
    
    def predict(self, time = 7):
        if time <= 0:
            return {"error": "Time must be greater than 0"}
        if self.model == None:
            return {"error": "Model is not loaded"}
        
        predictions = self.model.predict(time)
        return {"predictions": predictions.tolist()} 

    def train_model(self):
        pass
    
    def update_parameters(self, params):
        if self.model is None:
            return {"error": "Model is not loaded"}
        try:
            self.model.set_params(**params)
        except Exception as e:
            return {"error": str(e)}



model = Model()


@app.route('/predict', methods=['GET'])
def predict():
    try:
        time = int(request.args.get('time', 7))
    except ValueError:
        return jsonify({"error": "Invalid 'time' parameter, it must be an integer"})
    prediction_result = model.predict(time)
    return jsonify(prediction_result)


if __name__ == '__main__':
    app.run(debug=True)
