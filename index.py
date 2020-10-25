# -- coding: utf-8 --
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Inicio():
    return render_template("home.html")

@app.route("/nosotros")
def program():
    return render_template("aboutus.html")  

@app.route("/informacion")
def about():
    return render_template("about.html")
 
if __name__ == "__main__":
    app.run(debug=True) 
