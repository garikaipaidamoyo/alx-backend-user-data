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
