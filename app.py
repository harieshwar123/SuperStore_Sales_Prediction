# -*- coding: utf-8 -*-

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features =[]
    quantity =  request.form.get("Quantity")
    print(quantity)
    
    int_features.append(float(quantity))
    
    discount = request.form.get("Discount")
    print(discount)
    int_features.append(float(discount))
    
    profit = request.form.get("Profit")
    print(profit)
    int_features.append(float(profit))
    
    segment = request.form['segments']
    print(segment)
    
    if segment == 'consumer':
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif segment == 'corporate':
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    else:
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)   
        
        
        
        
        
    region = request.form['regions']
    print(region)
    
    if region == 'central':
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif region == 'east':
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif region == 'south':
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)    
    else:
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
    print(int_features)     
        
        
    
    shipclass = request.form['shipclass']
    print(shipclass)
    
    if shipclass == 'first':
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif shipclass == 'sameday':
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif shipclass == 'second':
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)    
    else:
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)          
        
        
    category = request.form['category']
    print(category)
    
    if category == 'furniture':
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif category == 'office_supplies':
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    else:
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)      
        

        
    print(int_features)    
    
    
   
    int_features2 = [float(x) for x in int_features]
    
    final_features = [np.array(int_features2)]
    
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)