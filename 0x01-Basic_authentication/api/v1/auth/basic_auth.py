#!/usr/bin/env python3

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if not authorization_header or not isinstance(
                authorization_header,
                str) or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.replace("Basic ", "")

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        if not base64_authorization_header or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        if not decoded_base64_authorization_header or not isinstance(
                decoded_base64_authorization_header,
                str) or ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str):
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        users = User.search({"email": user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> User:
        if not request:
            return None

        authorization_header = self.authorization_header(request)
        if not authorization_header:
            return None

        base64_header = self.extract_base64_authorization_header(
            authorization_header)

        if not base64_header:
            return None

        decoded_header = self.decode_base64_authorization_header(base64_header)
        if not decoded_header:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if not user_email or not user_pwd:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
