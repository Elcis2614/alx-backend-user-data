#!/usr/bin/env python3
"""
    Auth class
"""
from flask import request


class Auth:
    """
        Simple Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            that returns False - path and excluded_paths will be used later
        """

        if path in excluded_paths:
            return False
        return True


    def authorization_header(self, request=None) -> str:
        """
            returns None
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
            returns None
        """
        return None
