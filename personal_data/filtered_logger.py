#!/usr/bin/env python3
"""
filtered logger.py
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Filter out specified fields from the message.
    """
    for field in fields:
        message = re.sub(field + '=[^' + separator + ']*',
                         field + '=' + redaction, message)
    return message
