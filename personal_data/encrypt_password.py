#!/usr/bin/env python3
"""
encrypt_password.py
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with bcrypt and return the salted hash as bytes.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a password matches a hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
