#!/usr/bin/env python3
"""
Module that inherits from Auth class and implments
a Basic auth class
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar
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
    
    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str,
            ) -> str:
         """
         Decodes the Base64 part of the Authorization header.

         Args:
             base64_authorization_header (str): The
             Base64 part of the Authorization header.

         Returns:
             str: The decoded value of the Base64 string if
             it's valid, None otherwise.
         """
         if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None