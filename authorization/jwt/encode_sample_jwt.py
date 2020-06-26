import time
import jwt


now = int(time.time())
expiration = 60
secret_key = 'n8BP8IrKklSWx_B5UtEHO7hEG9_IXqSHuoLYc03veDU'
payload = {
    "iat": now,
    "exp": now + expiration,
    "iss": "https://something.com/auth/realms/terra",
    "aud": "account",
    "typ": "Bearer",
    "name": "Test",
    "email": "test@something.com"
}


# HS256 - OK
print('-'*3, 'HS256')
token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
print(f'token={token}')
dec_token = jwt.decode(token, verify=False)
print(f'dec_token={dec_token}')