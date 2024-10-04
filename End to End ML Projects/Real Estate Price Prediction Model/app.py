from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('CleanedData.csv')
    locations = df['location'].unique()
    sizes = df['size'].unique()
    baths = df['bath'].unique()
    
    return render_template('index.html',locations=locations,sizes=sizes,baths=baths)

@app.route('/predict',methods=['POST'])
def predict():
    location = request.form.get('location')
    size = int(request.form.get('size'))
    total_square = int(request.form.get('total_square'))
    bath = request.form.get('bath')
    # model = pickle.load(open('RFR.pkl','rb'))
    # prediction = model.predict(pd.DataFrame([[location,size,total_square,bath]],
    #                                         columns=['location','size','total_sqft','bath']))
    print(20)
    return str(20)


if __name__ =='__main__':
    app.run(debug=True,port=5001)