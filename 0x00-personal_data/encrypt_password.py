#!/usr/bin/env python3

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password using bcrypt.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to check.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
