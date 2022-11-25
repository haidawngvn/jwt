import jwt
from decouple import config
from typing import Dict
import time

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')

def token_reponse(token:str):
    return {
        'access_token':token
    }

def signJWT(user_id:str)->Dict[str,str]:
    payload = {
        'user_id': user_id,
        'expires': time.time()+600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_reponse(token)

def decodeJWT(token:str, with_secret_key = True)->dict:
    try:
        if with_secret_key:
            decode_token = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        else:
            decode_token = jwt.decode(token, options={"verify_signature": False})
        return decode_token #if decode_token['expires']>= time.time() else None
    except:
        return "Decode failed"

if __name__ == '__main__':
    # token = signJWT('tui@abc.com')
    # print(token)

    # a Nam gave
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdXNlci1lcnAtc3RhZ2luZy50dW9pdHJlLnZuL2FwaS9sb2dpbiIsImlhdCI6MTY2ODQ4NDE5NywiZXhwIjo3NzE2NDg0MTk3LCJuYmYiOjE2Njg0ODQxOTcsImp0aSI6Iks5cnBLdklWYllpRmZNbFEiLCJzdWIiOjI2MSwicHJ2IjoiOTA0ZjZkMmQ4NzI1ZjJjNWI0OThiYTg1Yzk5YTE4ZGNiY2ZjMmQ4NSJ9.UkoYsIaMlBgLxs7qC0c2O-1kLt3Oo1CwOOnTTQjFlGQ'

    # acc a Do
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTkyLjE2OC42MS4xMTYvYXBpL2xvZ2luIiwiaWF0IjoxNjY4NTgwNzE4LCJleHAiOjc3MTY1ODA3MTgsIm5iZiI6MTY2ODU4MDcxOCwianRpIjoiTWdsUG84eG9pZ1F0eWR3MCIsInN1YiI6MjYwLCJwcnYiOiI5MDRmNmQyZDg3MjVmMmM1YjQ5OGJhODVjOTlhMThkY2JjZmMyZDg1In0.nCnYdXo6PKhwy1lEvbwKGfY2PmKXz01qDjVFmYS1a3k'
    
    decoded1 = decodeJWT(token, with_secret_key= False)
    print(decoded1)

    # u1
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoibnZfQSIsImV4cGlyZXMiOjE2NjA1NDEyNDkuMDM1Mjg2fQ.EyJZbeyynl4bwPN0G7VYP6dQw6fmm3Gh92TxJkOiozA'

    decoded2 = decodeJWT(token, with_secret_key= False)
    print(decoded2)
    
    {
        'iss': 'http://user-erp-staging.tuoitre.vn/api/login', 
        'iat': 1668484197, 
        'exp': 7716484197, 
        'nbf': 1668484197, 
        'jti': 'K9rpKvIVbYiFfMlQ', 
        'sub': 261, 
        'prv': '904f6d2d8725f2c5b498ba85c99a18dcbcfc2d85'
    }
    # list = [270, 430]
    # for i in list:
    #     token = signJWT(430)
    #     print(i, ' :')
    #     print(token)
    #     print('')
    token = signJWT(46)
    print(token)
    
    
#     261
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdXNlci1lcnAtc3RhZ2luZy50dW9pdHJlLnZuL2FwaS9sb2dpbiIsImlhdCI6MTY2ODQ4NDE5NywiZXhwIjo3NzE2NDg0MTk3LCJuYmYiOjE2Njg0ODQxOTcsImp0aSI6Iks5cnBLdklWYllpRmZNbFEiLCJzdWIiOjI2MSwicHJ2IjoiOTA0ZjZkMmQ4NzI1ZjJjNWI0OThiYTg1Yzk5YTE4ZGNiY2ZjMmQ4NSJ9.UkoYsIaMlBgLxs7qC0c2O-1kLt3Oo1CwOOnTTQjFlGQ

# 200 - Hai Dang
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMDAsImV4cGlyZXMiOjE2Njg1ODYyNzkuOTE5NDU0OH0.D9D9n6Ps_Lm549nRd_CFxpuJqFK25N8oNU9sTDW1fW8

# 201 - Chi Kien
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMDEsImV4cGlyZXMiOjE2Njg1ODYzNDcuOTkxMzE4fQ.yogunlGflSer5uXyceQ3y7YYmLSxacLgGMkoEjCAiwo

# 202 - Anh Nam
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMDIsImV4cGlyZXMiOjE2Njg1ODYzODEuNjMwNTk5fQ.CxlkwHa9DmlzE4N5MGaAg0kNIymjOt_s0BqXPRZhNKk

# 260 - Anh Do
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTkyLjE2OC42MS4xMTYvYXBpL2xvZ2luIiwiaWF0IjoxNjY4NTgwNzE4LCJleHAiOjc3MTY1ODA3MTgsIm5iZiI6MTY2ODU4MDcxOCwianRpIjoiTWdsUG84eG9pZ1F0eWR3MCIsInN1YiI6MjYwLCJwcnYiOiI5MDRmNmQyZDg3MjVmMmM1YjQ5OGJhODVjOTlhMThkY2JjZmMyZDg1In0.nCnYdXo6PKhwy1lEvbwKGfY2PmKXz01qDjVFmYS1a3k
