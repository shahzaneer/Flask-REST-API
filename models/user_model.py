import mysql.connector as db
import json
from flask import Response, make_response
import jwt
from datetime import datetime, timedelta

class UserModel():
    def __init__(self):
        try:
            self.connection = db.connect(host="localhost", user="root" , password = "", database = "users" )
            self.connection.autocommit = True
            self.cursorr = self.connection.cursor(dictionary= True)
            print("connection successful")
        except Exception as e:
            print("Some error")

    def getUsersModel(self):
        """ Business Logic for Getting all the Users """
        self.cursorr.execute("select * from user_info")
        result = self.cursorr.fetchall()
        #! json_dump is used to stringify the result
        # print(type(result))
        if len(result) > 0:
            # result = json.dumps(result)
            res = make_response({"payload":result} , 200) #200 -> status code means ok
            res.headers["Access-Control-Origin"] = "*"
            return res
        else:  
            return make_response({"message": "No User Found"}, 202) #202 -> status code means accepted

    def addOneUserModel(self, data):
        """ Business Logic for adding one User """
        self.cursorr.execute(f"insert into user_info (id , Username, fullname, email, password) values ('{data['id']}' , '{data['Username']}' , '{data['fullname']}', '{data['email']}' , '{data['password']}') ")
        # print(data["fullname"])
        return make_response({"message": "User Created Successfully"}, 201) #201 -> status code means created     
    
    def  updateOneUserModel(self, data):
        """ Business Logic for updating one User """
        self.cursorr.execute(f"update user_info set Username = '{data['Username']}' , fullname = '{data['fullname']}' , email = '{data['email']}' , password = '{data['password']}' where id = {data['id']} ")
        if self.cursorr.rowcount == 0:
            return make_response({"message": "No User Found"}, 202) #202 -> status code means accepted
        else:
            return make_response({"message":"User Updated Successfully"}, 200) #200 -> status code means ok

    def deleteOneUserModel(self,data):
        """Business Logic for deleting one User """ 
        self.cursorr.execute(f"delete from user_info where id = {data['id']}")
        if self.cursorr.rowcount == 0:
            return make_response({"message":"No User Found"}, 202) #202 -> status code means accepted
        else:
            return make_response({"message":"User Deleted Successfully"}, 200) #200 -> status code means ok

    def patchOneUserModel(self,data,idx):
        """Business Logic for updating one Users specific details on runtime """ 
        # using string manipulation for making the dynamic query
        query = "update user_info set "
        for key in data:
            query += f"{key} = '{data[key]}' , "
        query = query[:-2] 
        query += f" where id = {idx}"
        self.cursorr.execute(query)
        # print(query)
        # return query
        if self.cursorr.rowcount == 0:
            return make_response({"message":"No User Found"}, 202) #202 -> status code means accepted
        else:
            return make_response({"message":"User Updated Successfully"}, 200) #200 -> status code means ok


    def getPaginationUserModel(self,limit,page):
        """Business Logic for getting paginated data """
        startingPoint = (page * limit) - limit
        self.cursorr.execute(f"select * from user_info LIMIT {startingPoint} , {limit}")
        result = self.cursorr.fetchall()
        if len(result) > 0:
            return make_response({"payload":result , "page_no" : page , "limit":limit}, 200) 
        else:
            make_response({"message":"No User Found"}, 202)       

    def upload_avatar_model(self, uid, db_path):
        self.cursorr.execute(f"UPDATE user_info SET avatar='{db_path}' WHERE id={uid}")
        if self.cursorr.rowcount>0:
            return make_response({"message":"file uploaded successfully", "path":db_path}, 201)
        else:
            return make_response({"message":"nothing to update"},204)    

    def loginModel(self, data):
        query = f"SELECT id, Username, fullname, email, roles_id FROM user_info WHERE Username = '{data['Username']}'  AND password = '{data['password']}'"
        self.cursorr.execute(query)
        result = self.cursorr.fetchall()  
        actualData = result[0]

        expiryTime = datetime.now() + timedelta(minutes=15)
        expiryTimeEpoch = int(expiryTime.timestamp())

        payload = {
            "payload" : actualData,
            "exp": expiryTimeEpoch
        }

        jwtToken = jwt.encode(payload, "SecretKeyJoKuchBhiHosktiHai", algorithm="HS256")

        return make_response({"message":"Login Successful", "token":jwtToken}, 200)
            