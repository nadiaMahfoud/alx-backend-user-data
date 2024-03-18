#!/usr/bin/env python3
"""Authentication module for the API. """
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header field from the request."""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Gets the current user from the request."""
        return None
