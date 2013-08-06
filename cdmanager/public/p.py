#!/usr/bin/python
import os, sys

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]
print _PROJECT_NAME

