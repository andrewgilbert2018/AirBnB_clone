#!/bin/usr/python3

"""an init magic method"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
