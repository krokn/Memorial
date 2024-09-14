import base64
import hashlib

from fastapi import HTTPException

from config import SECRET_FOR_TOKEN


class Encrypt:

    @staticmethod
    def create_token(identifier: str):
        encoded_identification_string = Encrypt.encoded(identifier)
        token = encoded_identification_string + "||" + Encrypt.hashed(encoded_identification_string + SECRET_FOR_TOKEN)
        return token

    @staticmethod
    def encoded(string):
        encoded_bytes = base64.b64encode(string.encode("utf-8"))
        encoded_string = encoded_bytes.decode("utf-8")
        return encoded_string

    @staticmethod
    def decoded(encoded_string):
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string

    @staticmethod
    def hashed(string):
        str_bytes = string.encode('utf-8')
        sha256 = hashlib.sha256()
        sha256.update(str_bytes)
        hashed_str = sha256.hexdigest()
        return hashed_str

    @staticmethod
    def get_user_by_token(token: str):
        try:
            encoded_identification_string = token.split("||")[0]
            user_signatura = token.split("||")[1]
            decoded_identification_string = Encrypt.decoded(encoded_identification_string)
            token_server = Encrypt.create_token(decoded_identification_string)
            server_signatura = token_server.split("||")[1]
            if user_signatura == server_signatura:
                return decoded_identification_string
        except Exception as e:
            raise HTTPException(status_code=405, detail='token incorrect')