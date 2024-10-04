from flask import Flask,render_template,request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    car = pd.read_csv('Cleaned.csv')
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique())
    fuel_types = sorted(car['fuel_type'].unique())
    return render_template('index.html',companies=companies,car_models=car_models,years=years,fuel_types=fuel_types)

@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))
    ####Calling Model
    model = pickle.load(open('RFR.pkl','rb'))
    prediction = model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],
                                            columns=['name','company','year','kms_driven','fuel_type']))
    print(prediction)
    return str(prediction[0])


if __name__ == "__main__":
    app.run(debug=True)