#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):

        return None


def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    """
    Returns True if the path is not in the list of strings excluded_paths.

    Returns True if path is None
    Returns True if excluded_paths is None or empty
    Returns False if path is in excluded_paths

    You can assume excluded_paths contains string path always ending by a /
    This method must be slash tolerant:
    path=/api/v1/status and path=/api/v1/status/
    must be returned False if excluded_paths contains /api/v1/status/
    """

    if path is None or not excluded_paths:
        return True

    # Make path slash-tolerant
    if not path.endswith('/'):
        path += '/'

    for excluded_path in excluded_paths:
        if not excluded_path.endswith('/'):
            excluded_path += '/'

        if path == excluded_path:
            return False

    return True
