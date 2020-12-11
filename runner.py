from flask import Flask, make_response, render_template, request, redirect
from libnya.colordescriptor import ColorDescriptor
from libnya.pencari import Searcher
from PIL import Image
import numpy as np
import cv2
import os
import shutil
import time
import csv

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
	with open('conf.csv','r') as conf:
		tp = 0
		tn = 0
		fp = 0
		fn = 0
		baca = csv.DictReader(conf)
		for l in baca:
			if l['tp'] == '1':
				tp+=1
			elif l['tn'] == '1':	
				tn+=1
			elif l['fp'] == '1':
				fp+=1
			else:
				fn+=1
	conf.close()
	akurasi = round((((tn+tp)/(tn+tp+fn+fp))*100),2)
	presisi = round(((tp/(fp+tp))*100),2)
	rekal = round(((tp/(fn+tp))*100),2)
	f1 = round((2*(rekal*presisi)/(rekal+presisi)),2)

	datasets = os.listdir('static/coba')
	if os.path.exists('static/temp') == True :
		image_names = os.listdir('static/temp')
		nearest = sorted(os.listdir('static/temp'))[0]
		target = os.listdir('static/tmp')
		return render_template("index.html", f1=(f1), akurasi=(akurasi), presisi=(presisi), rekal=(rekal), image_names=sorted(image_names),\
		target=(target), aw=1, count=len(datasets), nearest=(nearest))
	else :
		return render_template("index.html", aw=2, count=len(datasets))

@app.route('/search', methods=['POST'])
def search():
	gambar = request.files['image']
	file = gambar.read()
	nama = gambar.filename[0:3]
	cd = ColorDescriptor((8, 12, 3))
	npimg = np.frombuffer(file, np.uint8)
	query = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
	
	features = cd.describe(query)
	 
	searcher = Searcher('index.csv')
	results = searcher.search(features)

	positif=['mou','sea','des']
	observ= str(results[0][1])[:3]
	tp = 1 if nama in positif and nama == observ else 0
	tn = 1 if nama not in positif and nama != observ else 0
	fp = 1 if nama not in positif and nama == observ else 0
	fn = 1 if nama in positif and nama != observ else 0
	conma = [tp,tn,fp,fn]
	with open('conf.csv','a') as conf:
		tulis = csv.writer(conf)
		tulis.writerow(conma)
	conf.close

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
