#!/usr/bin/env python3
"""filtered logger.py"""


def filter_datum(fields, redaction, message, separator):
    """Filter out specified fields from the message."""
    parts = message.split(separator)
    result = []

    for part in parts:
        if "=" in part:
            key, value = part.split("=", 1)
            if key in fields:
                value = redaction
            result.append(f"{key}={value}")

    return separator.join(result)
