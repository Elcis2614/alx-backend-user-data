#!/usr/bin/env python3
"""
    Auth class
"""
from flask import request
from typing import (
    List,
    TypeVar,    
)


class Auth:
    """
        Simple Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            that returns False - path and excluded_paths will be used later
        """
        if path:
            new_p = path
            if path[-1] == '/':
                return new_p not in excluded_paths
            return new_p + '/' not in excluded_paths
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
