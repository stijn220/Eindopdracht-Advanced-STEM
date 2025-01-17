from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

class Model:
    def __init__(self):
        self.model = None
        self.load_model('notebooks/eda_model.pkl')


    def load_model(self, model_path):
        self.model = joblib.load(model_path)
    
    def predict(self, time = 7):
        if time <= 0:
            return {"error": "Time must be greater than 0"}
        if self.model == None:
            return {"error": "Model is not loaded"}
        
        predictions = self.model.predict(time)
        return {"predictions": predictions.tolist()} 

    
    def update_parameters(self, params):
        if self.model is None:
            return {"error": "Model is not loaded"}
        try:
            self.model.set_params(**params)
            return {"message": "Parameters updated successfully"}
        except Exception as e:
            return {"error": str(e)}


model = Model()


@app.route('/predict', methods=['GET'])
def predict():
    try:
        time = int(request.args.get('time', 7))
    except ValueError:
        return jsonify({"error": "Invalid 'time' parameter, it must be an integer"}), 400
    prediction_result = model.predict(time)
    return jsonify(prediction_result)

@app.route('/update-model', methods=['POST'])
def update_model():
    try:
        params = request.json  
        if not isinstance(params, dict):
            raise ValueError("Parameters must be provided as a dictionary")
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Update model parameters
    update_result = model.update_parameters(params)
    return jsonify(update_result)


if __name__ == '__main__':
    app.run(debug=True)
