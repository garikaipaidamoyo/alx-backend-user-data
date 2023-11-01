#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        pattern = re.compile(rf"{field}=.*?{separator}")
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message
