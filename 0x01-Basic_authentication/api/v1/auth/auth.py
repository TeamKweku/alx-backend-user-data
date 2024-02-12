#!/usr/bin/env python3
"""
module that implements an Auth class
"""
from typing import List, TypeVar
from flask import request
import re


User = TypeVar("User")


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.

        Args:
            path (str): The path to check for authentication requirement.
            excluded_paths (List[str]): List of paths that are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Add a trailing slash to path if not present
        if not path.endswith("/"):
            path += "/"

        # Check if path is in excluded_paths
        if path in excluded_paths:
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
        if request is None:
          return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """
        Retrieves the current authenticated user.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current authenticated user.
        """
        # Placeholder implementation, always returning None for now
        return None
