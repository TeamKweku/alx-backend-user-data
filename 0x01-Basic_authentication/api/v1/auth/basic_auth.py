#!/usr/bin/env python3
"""
Module that inherits from Auth class and implments
a Basic auth class
"""
import re
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for a Basic Authentication.

        Args:
            authorization_header (str): The
            Authorization header.

        Returns:
            str: The Base64 part of the Authorization header
            if it's valid, None otherwise.
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None
