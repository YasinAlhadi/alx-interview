#!/usr/bin/python3
"utf validation"


def validUTF8(data):
    """check if data is valid utf-8"""
    try:
        bytes([i & 255 for i in data]).decode()
        return True
    except Exception:
        return False
