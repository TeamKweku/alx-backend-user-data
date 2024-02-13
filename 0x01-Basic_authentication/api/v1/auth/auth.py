#!/usr/bin/env python3
"""
module that implements an Auth class
"""
from typing import List, TypeVar
from flask import request
import re


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
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ""
                if exclusion_path[-1] == "*":
                    pattern = "{}.*".format(exclusion_path[0:-1])
                elif exclusion_path[-1] == "/":
                    pattern = "{}/*".format(exclusion_path[0:-1])
                else:
                    pattern = "{}/*".format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

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
