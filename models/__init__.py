#!/usr/bin/python3
"""
This module initializes the engine package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
