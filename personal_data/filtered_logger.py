#!/usr/bin/env python3
"""
filtered logger.py
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Filter out specified fields from the message.
    """
    for field in fields:
        message = re.sub(field + '=[^' + separator + ']*',
                         field + '=' + redaction, message)
    return message
