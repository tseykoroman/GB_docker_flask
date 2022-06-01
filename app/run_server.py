# USAGE
# Start the server:
# 	python run_front_server.py
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
import dill
import pandas as pd
import os
dill._dill._reverse_typemap['ClassType'] = type
#import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def load_model(model_path):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	print(model)

modelpath = "/app/app/models/pipeline.dill"
load_model(modelpath)

@app.route("/", methods=["GET"])
def general():
	return """Welcome to fraudelent prediction process. Please use 'http://<address>/predict' to POST"""

@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}
	dt = strftime("[%Y-%b-%d %H:%M:%S]")
	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":

		ID, gender, age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, systolic, relaxation, fasting_blood_sugar, cholesterol, triglyceride, hdl, ldl, hemoglobin, urine_protein, serum_creatinine, ast, alt, gtp, oral, dental_caries, tartar = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
		request_json = flask.request.get_json()
		if request_json["ID"]:
			ID = request_json['ID']

		if request_json["gender"]:
			gender = request_json['gender']

		if request_json["age"]:
			age = request_json['age']

		if request_json["height"]:
			height = request_json['height']

		if request_json["weight"]:
			weight = request_json['weight']

		if request_json["waist"]:
			waist = request_json['waist']

		if request_json["eyesight_left"]:
			eyesight_left = request_json['eyesight_left']

		if request_json["eyesight_right"]:
			eyesight_right = request_json['eyesight_right']

		if request_json["hearing_left"]:
			hearing_left = request_json['hearing_left']

		if request_json["hearing_right"]:
			hearing_right = request_json['hearing_right']

		if request_json["systolic"]:
			systolic = request_json['systolic']

		if request_json["relaxation"]:
			relaxation = request_json['relaxation']

		if request_json["fasting_blood_sugar"]:
			fasting_blood_sugar = request_json['fasting_blood_sugar']

		if request_json["cholesterol"]:
			cholesterol = request_json['cholesterol']

		if request_json["triglyceride"]:
			triglyceride = request_json['triglyceride']

		if request_json["hdl"]:
			hdl = request_json['hdl']

		if request_json["ldl"]:
			ldl = request_json['ldl']

		if request_json["hemoglobin"]:
			hemoglobin = request_json['hemoglobin']

		if request_json["urine_protein"]:
			urine_protein = request_json['urine_protein']

		if request_json["serum_creatinine"]:
			serum_creatinine = request_json['serum_creatinine']

		if request_json["ast"]:
			ast = request_json['ast']

		if request_json["alt"]:
			alt = request_json['alt']

		if request_json["gtp"]:
			gtp = request_json['gtp']

		if request_json["oral"]:
			oral = request_json['oral']

		if request_json["tartar"]:
			tartar = request_json['tartar']

		if request_json["dental_caries"]:
			dental_caries = request_json['dental_caries']

		logger.info(f'{dt} Data: gender={gender}, age={age}, height={height}, weight={weight}, waist={waist}, eyesight_left={eyesight_left}, eyesight_right={eyesight_right}, hearing_left={hearing_left}, hearing_right={hearing_right}, systolic={systolic}, relaxation={relaxation}, fasting_blood_sugar={fasting_blood_sugar}, cholesterol={cholesterol}, triglyceride={triglyceride}, hdl={hdl}, ldl={ldl}, hemoglobin={hemoglobin}, urine_protein={urine_protein}, serum_creatinine={serum_creatinine}, ast={ast}, alt={alt}, gtp={gtp}, oral={oral}, tartar={tartar}, dental_caries={dental_caries}')
		try:
			preds = model.predict_proba(pd.DataFrame({"gender": [gender],
                                              "age": [age],
                                              "height": [height],
                                              "weight": [weight],
                                              "waist": [waist],
                                              "eyesight_left": [eyesight_left],
                                              "eyesight_right": [eyesight_right],
                                              "hearing_left": [hearing_left],
                                              "hearing_right": [hearing_right],
                                              "systolic": [systolic],
                                              "relaxation": [relaxation],
                                              "fasting_blood_sugar": [fasting_blood_sugar],
                                              "cholesterol": [cholesterol],
                                              "triglyceride": [triglyceride],
                                              "hdl": [hdl],
                                              "ldl": [ldl],
                                              "hemoglobin": [hemoglobin],
                                              "urine_protein": [urine_protein],
                                              "serum_creatinine": [serum_creatinine],
                                              "ast": [ast],
                                              "alt": [alt],
                                              "gtp": [gtp],
                                              "oral": [oral],
                                              "tartar": [tartar],
                                              "dental_caries": [dental_caries]}))
		except AttributeError as e:
			logger.warning(f'{dt} Exception: {str(e)}')
			data['predictions'] = str(e)
			data["ID"] = ID
			data['success'] = False
			return flask.jsonify(data)

		data["predictions"] = preds[:, 1][0]
		data["ID"] = ID
		# indicate that the request was a success
		data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)
