#!/usr/bin/env python3
"""
Module that implements a PII functions
"""
from typing import List
import re


patterns = {
    "extract": lambda x, y: r"(?P<field>{})=[^{}]*".format("|".join(x), y),
    "replace": lambda x: r"\g<field>={}".format(x),
}

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Fitlers a log line based on provided parameters of the func
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
