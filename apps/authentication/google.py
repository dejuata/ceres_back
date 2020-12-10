from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    @staticmethod
    def validate(auth_token):
        idinfo = id_token.verify_oauth2_token(
            auth_token, requests.Request())

        print("info", idinfo)
        if 'accounts.google.com' in idinfo['iss']:
            return idinfo
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request())
            print("info", idinfo)

            if 'accounts.google.com' in idinfo['iss']:
                return idinfo

        except Exception:
            return "The token is either invalid or has expired"
