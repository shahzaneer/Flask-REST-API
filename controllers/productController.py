from flask import Flask, Blueprint
productController = Blueprint("productController",__name__)

@productController.route("/products/item")
def product():
    return "<h1>COCA reduce hona chahiay!</h1>"

