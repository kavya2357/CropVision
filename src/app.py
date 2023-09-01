from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

clf_crop = pickle.load(open(r"C:\Users\kavya\Desktop\crop_prediction_and_profitability_analysis\src\model\clf_crop.pkl", 'rb'))
preprocesser = pickle.load(open(r"C:\Users\kavya\Desktop\crop_prediction_and_profitability_analysis\src\model\preprocesser.pkl", 'rb'))
clf_profit=pickle.load(open(r"C:\Users\kavya\Desktop\crop_prediction_and_profitability_analysis\src\model\clf_profit.pkl",'rb'))

@app.route('/api/predict', methods=['POST'])
def predict():
    crop_dict={
    1:'Rice',
    2:'Wheat',
    3:'Cotton',
    4:'Tea',
    5:'Soybean',
    6:'Barley',
    7:'Maize',
    8:'Coconut',
    9:'Apple',
    10:'Millets',
    11:'Sugarcane',
    12:'Groundnut',
    13:'Jute' ,
    14:'Potato',
    15:'Corn',
    16:'Mango',
    17:'Cashew' ,
    18:'Orange',
    19:'Grapes',
    20:'Banana',
    21:'Pineapple',
    22:'Rubber',
    23:'Strawberry',
    24:'Onion',
    25:'Pepper',
    26:'Chickpeas'
    }
    
    data=request.get_json()
    Location = data['Location']
    Soil_Type = data['Soil_Type']
    Rainfall = data['Rainfall']
    Area_Cultivated = data['Area_Cultivated']
    Investment = data['Investment']

    features = np.array([[Location, Soil_Type, Rainfall, Area_Cultivated, Investment]])

    transformed_features = preprocesser.transform(features)

    predicted_value = clf_crop.predict(transformed_features).reshape(1, -1)

    if predicted_value[0][0] in crop_dict:
        crop = crop_dict[predicted_value[0][0]]
        profit=str(predicted_value[0][1])
        result=f"{crop} is the best crop to be cultivated right there with a profit of {profit}"
    else:
        result="Sorry, we are not able to recommend a proper crop for this environment."
    return jsonify({'prediction':result})

if __name__ == '__main__':
    app.run(debug=True)
