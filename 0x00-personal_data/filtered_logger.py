#!/usr/bin/env python3
"""
    Regex-ing
"""
import re
import logging
from typing import (
    List,
)
PII_FIELDS = ("name", "email","phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
     Takes no arguments and returns a logging.Logger object
    """
    logObj = logging.getLogger("user_data")
    logObj.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(
                       RedactingFormatter(list(PII_FIELDS)))])
    logObj.propagate = False
    return logObj
