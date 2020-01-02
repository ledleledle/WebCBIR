from flask import Flask, make_response, render_template, request, redirect
from libnya.colordescriptor import ColorDescriptor
from libnya.pencari import Searcher
from PIL import Image
import numpy as np
import cv2
import os
import shutil
import time

app = Flask(__name__)

@app.route('/')
def cekawal():
	if os.path.exists('static/temp') == True :
		shutil.rmtree('static/temp')
		shutil.rmtree('static/tmp')
		return redirect('/home')
	else :
		return redirect('/home')

@app.route('/home')
def home():
	datasets = os.listdir('static/coba')
	if os.path.exists('static/temp') == True :
		image_names = os.listdir('static/temp')
		nearest = os.listdir('static/temp')[1]
		target = os.listdir('static/tmp')
		return render_template("index.html", image_names=sorted(image_names), target=(target), aw=1, count=len(datasets), nearest=(nearest))
	else :
		return render_template("index.html", aw=2, count=len(datasets))

@app.route('/search', methods=['POST'])
def search():
	file = request.files['image'].read()
	cd = ColorDescriptor((8, 12, 3))
	npimg = np.frombuffer(file, np.uint8)
	query = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
	
	features = cd.describe(query)
	 
	searcher = Searcher('index.csv')
	results = searcher.search(features)

	os.makedirs('static/temp')
	os.makedirs('static/tmp')
	
	i = 1
	for (score, resultID) in results:
		i += 1
		result = cv2.imread("static/coba/" + resultID)
		saveimg = cv2.imwrite("static/temp/" + str(score) + str(i) + ".jpeg", result)

	imgstr = time.strftime("%Y%m%d-%H%M%S")
	cv2.imwrite("static/tmp/"+ imgstr +".jpeg", query)
	return redirect("/home")

@app.route('/<page_name>')
def other_page(page_name):
	response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
	return response

if __name__ == '__main__':
	app.run(debug=True)