from flask import Flask ,Blueprint
from models.user_model import UserModel
from flask import request , send_file
from datetime import datetime
from models.auth_model import auth_model


appController = Blueprint("controllers",__name__)
usermodel = UserModel()
auth = auth_model()

@appController.route("/user/all")
# End point 
@auth.token_auth()
def getUsersController():
    return usermodel.getUsersModel()

@appController.route("/user/addone", methods = ["POST"])
def addOneUserController():
    # print(request.form)
    return usermodel.addOneUserModel(request.form)   

@appController.route("/user/updateone", methods = ["PUT"])
def updateOneUserController():
    return usermodel.updateOneUserModel(request.form)        

@appController.route("/user/deleteone", methods = ["DELETE"])
def deleteOneUserController():
    return usermodel.deleteOneUserModel(request.form)

@appController.route("/user/patchone/<idx>", methods = ["PATCH"])
def patchOneUserController(idx):
    return usermodel.patchOneUserModel(request.form,idx)


@appController.route("/user/getall/<int:limit>/page/<int:page>", methods = ["GET"])
def getPaginationUserController(limit,page):
    return usermodel.getPaginationUserModel(limit,page)

@appController.route("/user/<uid>/avatar/upload", methods=["PATCH"])
def uploadAvatar(uid):
    # print(request.files)
    file = request.files['avatar'] #request se jo file aarhi hogi
    print(file.filename)
    # file ko uniquely save krne k liay hamain kuch aisi cheez chahiay jo har waqt unique rahe ? har waqt unique kia hai ? timestamp
    # print(datetime.now().timestamp()) # isme jo . aarha hai wo nhi chahiay usse remove krdengay 
    uniqueIdentifierFile =  str(datetime.now().timestamp()).replace(".", "") 
    split_filename = file.filename.split(".") 
    ext_pos = len(split_filename)-1 
    ext = split_filename[ext_pos]
    new_filename = f"{uniqueIdentifierFile}.{ext}"
    db_path = f"Uploads/{new_filename}"
    file.save(db_path)
    return usermodel.upload_avatar_model(uid, db_path)       # return "file uploaded successfully"

@appController.route("/user/uploads/<uid_img>")
def getAvatar(uid_img):
    return send_file(f"Uploads/{uid_img}")

@appController.route("/user/login", methods = ["POST"])
def loginController():
    return usermodel.loginModel(request.form)