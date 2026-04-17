#!/usr/bin/env python3
"""Session authentication module
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from typing import Dict, TypeVar


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""

        if user_id is None:
            return None

        if type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        if session_id is None:
            return None

        if type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return a User based on session cookie"""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user: User = User.get(user_id)

        if user_id is None:
            return None

        return user
