#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False for now"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Returns None for now"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None for now"""
        return None

    def session_cookie(self, request=None):
        """Return Cookie value or None"""
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        cookie_name = request.cookies.get(session_name)

        return cookie_name
