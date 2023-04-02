from flask import Flask
from controllers.user_controller import appController
from controllers.productController import productController
import os

app = Flask(__name__)

@app.route("/")
def agency():
    return "<h1>Pull up on you like agency </h1>"

@app.route("/signup")
def signup():
    return "sign up"

#!  we should have to register other controllers of routing jinka blueprint hmne banaya hai werna error ayega!
app.register_blueprint(appController)
app.register_blueprint(productController)
#! we are going to register all the files in the controller folder using the OS module (error)
# register_controllers(app)



    

if __name__ == '__main__':
    app.run(debug=True)
    
