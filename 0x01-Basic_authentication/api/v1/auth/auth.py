#!/usr/bin/env python3
"""
module that implements an Auth class
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.

        Args:
            path (str): The path to check for authentication requirement.
            excluded_paths (List[str]): List of paths that are
            excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            str: The authorization header value.
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the current authenticated user.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current authenticated user.
        """
        return None
