#!/usr/bin/env python3
"""
    Regex-ing
"""
import re
from typing import (
    List
)


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
        returns the log message obfuscated
    """
    for field in fields:
        pattern = '{}\=([^{}]+){}'.format(field, separator, separator)
        message = re.sub(pattern, '{}={}{}'.format(field, redaction, separator), message, 0, 0)
    return message
