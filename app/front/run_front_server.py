import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField, FloatField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    id = StringField('id')
    gender = StringField('gender')
    age = StringField('age : 5-years gap')
    height = IntegerField('height (cm)')
    weight = IntegerField('weight (kg)')
    waist = IntegerField('waist (cm) : waist circumference length')
    eyesight_left = FloatField('eyesight (left)')
    eyesight_right = FloatField('eyesight (right)')
    hearing_left = IntegerField('hearing (left)')
    hearing_right = IntegerField('hearing (right)')
    systolic = IntegerField('systolic : blood pressure')
    relaxation = IntegerField('relaxation : blood pressure')
    fasting_blood_sugar = IntegerField('fasting blood sugar')
    cholesterol = IntegerField('cholesterol : total')
    triglyceride = IntegerField('triglyceride')
    hdl = IntegerField('HDL : cholesterol type')
    ldl = IntegerField('LDL : cholesterol type')
    hemoglobin = FloatField('hemoglobin')
    urine_protein = IntegerField('urine protein')
    serum_creatinine = FloatField('serum creatinine')
    ast = IntegerField('AST : glutamic oxaloacetic transaminase type')
    alt = IntegerField('ALT : glutamic oxaloacetic transaminase type')
    gtp = IntegerField('GTP : γ-GTP')
    oral = StringField('oral : oral examination status')
    dental_caries = IntegerField('dental caries')
    tartar = StringField('tartar : tartar status')


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(id, gender, age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, systolic, relaxation, fasting_blood_sugar, cholesterol, triglyceride, hdl, ldl, hemoglobin, urine_protein, serum_creatinine, ast, alt, gtp, oral, dental_caries, tartar):
    body = {'ID': id,
            'gender': gender,
            'age': age,
            'height': height,
            'weight': weight,
            'waist': waist,
            'eyesight_left': eyesight_left,
            'eyesight_right': eyesight_right,
            'hearing_left': hearing_left,
            'hearing_right': hearing_right,
            'systolic': systolic,
            'relaxation': relaxation,
            'fasting_blood_sugar': fasting_blood_sugar,
            'cholesterol': cholesterol,
            'triglyceride': triglyceride,
            'hdl': hdl,
            'ldl': ldl,
            'hemoglobin': hemoglobin,
            'urine_protein': urine_protein,
            'serum_creatinine': serum_creatinine,
            'ast': ast,
            'alt': alt,
            'gtp': gtp,
            'oral': oral,
            'dental_caries': dental_caries,
            'tartar': tartar}

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)

@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['id'] = request.form.get('id')
        data['gender'] = request.form.get('gender')
        data['age'] = request.form.get('age')
        data['height'] = request.form.get('height')
        data['weight'] = request.form.get('weight')
        data['waist'] = request.form.get('waist')
        data['eyesight_left'] = request.form.get('eyesight_left')
        data['eyesight_right'] = request.form.get('eyesight_right')
        data['hearing_left'] = request.form.get('hearing_left')
        data['hearing_right'] = request.form.get('hearing_right')
        data['systolic'] = request.form.get('systolic')
        data['relaxation'] = request.form.get('relaxation')
        data['cholesterol'] = request.form.get('cholesterol')
        data['fasting_blood_sugar'] = request.form.get('fasting_blood_sugar')
        data['triglyceride'] = request.form.get('triglyceride')
        data['hdl'] = request.form.get('hdl')
        data['ldl'] = request.form.get('ldl')
        data['hemoglobin'] = request.form.get('hemoglobin')
        data['urine_protein'] = request.form.get('urine_protein')
        data['serum_creatinine'] = request.form.get('serum_creatinine')
        data['ast'] = request.form.get('ast')
        data['alt'] = request.form.get('alt')
        data['gtp'] = request.form.get('gtp')
        data['oral'] = request.form.get('oral')
        data['dental_caries'] = request.form.get('dental_caries')
        data['tartar'] = request.form.get('tartar')

        try:
            response = str(get_prediction(data['id'],
                                      data['gender'],
                                      data['age'],
                                      data['height'],
                                      data['weight'],
                                      data['waist'],
                                      data['eyesight_left'],
                                      data['eyesight_right'],
                                      data['hearing_left'],
                                      data['hearing_right'],
                                      data['systolic'],
                                      data['relaxation'],
                                      data['cholesterol'],
                                      data['fasting_blood_sugar'],
                                      data['triglyceride'],
                                      data['hdl'],
                                      data['ldl'],
                                      data['hemoglobin'],
                                      data['urine_protein'],
                                      data['serum_creatinine'],
                                      data['ast'],
                                      data['alt'],
                                      data['gtp'],
                                      data['oral'],
                                      data['dental_caries'],
                                      data['tartar']))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
