#!/usr/bin/env python3
"""
Main file
"""

import re
import os
import logging


class RedactingFormatter(logging.Formatter):

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        redacted_message = record.getMessage()
        fields = os.environ.get("FIELDS", "").split(",")
        for field in fields:
            redacted_message = re.sub(f"{field}=[^;]+",
                                      f"{field}={self.REDACTION}",
                                      redacted_message)
        record.message = redacted_message
        return super().format(record)


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        pattern = re.compile(rf"{field}=.*?{separator}")
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;"
    "date_of_birth=12/12/1986;"
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

if __name__ == "__main__":
    message = "name=Bob;email=bob@dylan.com;"
    "ssn=000-123-0000;password=bobby2019;"
    log_record = logging.LogRecord("my_logger", logging.INFO, None, None,
                                   message, None, None)
    formatter = RedactingFormatter()
    print(formatter.format(log_record))
