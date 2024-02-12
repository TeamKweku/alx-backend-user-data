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
from models.user import User


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
            pattern = r"Basic (?P<token>.+)"
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group("token")
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
                return res.decode("utf-8")
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str,
    ) -> Tuple[str, str]:
        """
        Extracts the user email and password from the
        Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
            The Base64 decoded value.

        Returns:
            (str, str): The user email and password if they're valid
            (None, None) otherwise.
        """
        if type(decoded_base64_authorization_header) == str:
            pattern = r"(?P<user>[^:]+):(?P<password>.+)"
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group("user")
                password = field_match.group("password")
                return user, password
        return None, None

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """
        Returns the User instance based on his email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if it's valid, None otherwise.
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({"email": user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the User instance for a request.

        Args:
            request: The request.

        Returns:
            User: The User instance if it's valid, None otherwise.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
