#!/usr/bin/env python3
"""
    Regex-ing
"""
import re
import logging
from typing import (
    List
)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        returns the log message obfuscated
    """
    for field in fields:
        p = '{}=([^{}]+){}'.format(field, separator, separator)
        message = re.sub(p, '{}={}{}'.format(field,
                         redaction, separator), message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self._fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Formats the logging record
        """
        log = super().format(record)
        return filter_datum(self._fields, self.REDACTION, log, self.SEPARATOR)
