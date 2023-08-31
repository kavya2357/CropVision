from flask import Flask, request

import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

clf_crop = pickle.load(open(r"C:\Users\kavya\Desktop\crop_prediction_and_profitability_analysis\model\clf_crop.pkl", 'rb'))
preprocesser = pickle.load(open(r"C:\Users\kavya\Desktop\crop_prediction_and_profitability_analysis\model\preprocesser.pkl", 'rb'))
clf_profit=pickle.load(open(r"C:\Users\kavya\Desktop\crop_prediction_and_profitability_analysis\model\clf_profit.pkl",'rb'))

@app.route("/", methods=['GET', 'POST'])
def index():
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
    
    if request.method == 'POST':
        location = request.form['location']
        soil_type = request.form['soil_type']
        rainfall = float(request.form['rainfall'])
        area = float(request.form['area'])
        investment = float(request.form['investment'])
        
        def recommendation(Location, Soil_Type, Rainfall, Area_Cultivated, Investment):
            features = np.array([[Location, Soil_Type, Rainfall, Area_Cultivated, Investment]])
            transformed_features = preprocesser.transform(features)

            prediction = clf_crop.predict(transformed_features).reshape(1, -1)

            return prediction

        predict = recommendation(location, soil_type, rainfall, area, investment)

        if predict[0][0] in crop_dict:
            crop = crop_dict[predict[0][0]]
            profit=str(predict[0][1])
            return f"{crop} is the recommended crop to be cultivated with a profit of {profit}"
        else:
            return f"Sorry, we are not able to recommend a proper crop for this environment."
        


    return """
    <form method="post">
        Location: <input type="text" name="location"><br>
        Soil Type: <input type="text" name="soil_type"><br>
        Rainfall: <input type="number" name="rainfall"><br>
        Area Cultivated: <input type="number" name="area"><br>
        Investment: <input type="number" name="investment"><br>
        <input type="submit" value="Submit">
    </form>
    """

if __name__ == '__main__':
    app.run(port=8080, debug=True)
