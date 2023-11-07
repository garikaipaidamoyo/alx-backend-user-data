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
