#!/usr/bin/env python3
"""a magic method for init"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
