from flask import Flask, render_template, request
from mlmodel import *

app = Flask(__name__,template_folder='template')

@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/getprediction", methods=["POST"])
def getpredict():
    aai = request.form['aai']
    aaha = request.form['aaha']
    aanr = request.form['aanr']
    aanb = request.form['aanb']
    ap = request.form['ap']

    newob = [[aai, aaha, aanr, aanb, ap]]
    print(newob)
    model = makeprediction()
    yp = model.predict(newob)[0]
    
    return render_template("page2.html",data=yp)
    

if(__name__ =="__main__"):
    app.run(debug=True)

