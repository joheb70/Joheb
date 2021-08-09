#This project is building a website from scratch and deploying it using heroku.css code is used to further improve the front end look
#Author: Abdul Joheb Ansari

##############################################################

#Flask class in imported from flask
from flask import Flask,render_template        

#app variable is intiated
app = Flask(__name__)

#Initiating home page with rendered htlm template
@app.route('/')
def home():
    return render_template("home.html")

#Initiating About page with rendered htlm template
@app.route('/about/')
def about():
    return render_template("about.html")
    

if __name__ == "__main__":
    app.run(debug=True)
