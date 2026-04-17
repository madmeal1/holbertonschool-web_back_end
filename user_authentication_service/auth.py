#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the salted hash"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
