import mysql.connector as db
from config.config import dbconfig
from flask import request, make_response
import re
import jwt
import json

class auth_model():
    def __init__(self):
        try:
            self.connection = db.connect(host = dbconfig["host"] , user = dbconfig["username"] , password = dbconfig["password"] , database = dbconfig["database"])
            self.connection.autocommit = True
            self.cursorr = self.connection.cursor(dictionary = True)
            print("auth Model : connection Successful")
        except Exception as e:
            print("auth Model : Some error")
            print(e)    


    def token_auth(self, endpoint=""):
        def inner1(func):
            def inner2(*args):
                endpoint = request.url_rule
                try:
                    authorization = request.headers.get("authorization")
                    if re.match("^Bearer *([^ ]+) *$", authorization, flags = 0):
                        token = authorization.split(" ")[1]
                        try:
                            tokendata = jwt.decode(token, "SecretKeyJoKuchBhiHosktiHai", algorithms = ["HS256"])
                            print(tokendata)
                            current_role = tokendata["payload"]["roles_id"]
                            self.cursorr.execute(f"SELECT * FROM accessibility_view WHERE endpoint = '{endpoint}'")
                            results = self.cursorr.fetchall()
                            print(results)
                            if len(results) > 0:
                                roles_allowed = json.loads(results[0]["roles"]) 
                                if current_role in roles_allowed:
                                    return func(*args)
                                else:
                                    return make_response({"message":"You are not allowed to access this endpoint"}, 422) 
                            else:
                                return make_response({"message":"Endpoint not found"}, 404)          
                        except Exception as e:
                            return make_response({"message":str(e) }, 401)
                    else:
                        return make_response({"message":"Invalid Token"}, 401)  
                except Exception as e:
                    return make_response({"message":str(e) }, 401)         
            return inner2            
        return inner1
