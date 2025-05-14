from functools import wraps
from flask import request, make_response, g
import jwt
from config.config import JWTSECRETKEY

class Auth:

    @staticmethod
    def auth():
        def decorator(fun):
            print("Inside auth")
            @wraps(fun)
            def wrapper(*args, **kwargs):
                 #print("Inside wrapper")
                 if not request.headers.get('Authorization'):
                     return make_response({'payload': "Token is missing!"})
                 
                 ## Extract token ##
                 requestBearer = request.headers['Authorization']
                 token = requestBearer.split(" ")
                 #print("request", token[1])
                 ## validate token ##
                 try:
                     data = jwt.decode(token[1], JWTSECRETKEY, algorithms=["HS256"])
                     print("abcc:", data)
                     g.user = data
                 except Exception as e:
                     return make_response({"payload": str(e)})                 
                 return fun(*args, **kwargs)
            #print("above wrapper")
            return wrapper
        #print("above decorator")
        return decorator


