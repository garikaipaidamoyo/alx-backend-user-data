#!/usr/bin/env python3
"""
Main file
"""

import re
import os
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for logging.
    """
    REDACTION = 'xxx'
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record, redacting sensitive fields.
        """
        redacted_message = record.getMessage()
        fields = os.environ.get("FIELDS", "").split(",")
        for field in fields:
            redacted_message = re.sub(
                f"{field}=.*?{self.SEPARATOR}",
                f"{field}={self.REDACTION}{self.SEPARATOR}", redacted_message)
        record.message = redacted_message
        return super().format(record)


def filter_datum(fields, redaction, message, separator):
    """
    Redact specific fields in a log message.
    """
    for field in fields:
        pattern = re.compile(rf"{field}=.*?{separator}")
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


if __name__ == "__main__":
    message = ("name=Bob;email=bob@dylan.com;"
               "ssn=000-123-0000;password=bobby2019;")
    log_record = logging.LogRecord("my_logger", logging.INFO, None, None,
                                   message, None, None)
    formatter = RedactingFormatter()
    print(formatter.format(log_record))
