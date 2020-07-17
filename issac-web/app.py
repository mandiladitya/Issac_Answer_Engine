import requests
import urllib
import json
import os
from flask import Flask,render_template,send_file,request,url_for,session,redirect

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/issac',methods = ['POST', 'GET'])
def search():
	if (request.method == 'POST'):
		a=[]
		latitute =request.form["latitute"].replace(" ", "%20")
		#lat=23.259933
		#lon=77.412613
		#longitute =request.form["longitute"]
		link="http://theissacapi.pythonanywhere.com/issac/{}".format(latitute)
		f=urllib.request.urlopen(link).read().decode('UTF-8')
		my=json.loads(f)
		l=list(my)
		#my=f.json()
		#jsonResponse = json.loads(my.decode('utf-8'))		
#y=json.loads(my)
		#esponse = json.dumps(my.text, sort_keys = True, indent = 4, separators = (',', ': '))
		#,latitute=latitute,longitute=longitute,length=length,breadth=breadth,width=width,height=height,bridge=bridge
		return render_template('index.html',y=my)
	return render_template('index.html')

@app.errorhandler(404)
def error(e):
	return render_template('error.html')
@app.errorhandler(500)
def server():
	return render_template('server-error.html')

app.run(host='0.0.0.0',debug=True)
