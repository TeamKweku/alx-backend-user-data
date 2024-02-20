#!/usr/bin/env python3
"""
Model that authenticates users
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Method that hashes a password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
