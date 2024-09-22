import jwt
import datetime
import secrets

SECRET_KEY = secrets.token_hex(32)

def create_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

if __name__ == '__main__':
    user_id = 123
    token = create_jwt(user_id)
    print(f"Generated JWT: {token}")

    decoded_payload = decode_jwt(token)
    print(f"Decoded JWT: {decoded_payload}")
