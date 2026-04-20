from jupiterutils.Utility import JPT_RUN_LINE, JPT_RUN_CODE
from enum import Enum

class spin(Enum):
    integer = 0
    double = 1

class size_behavior(Enum):
    greedy = 0
    vertical = 1
    horizontal = 4
    fixed = 5

class JDGCreator:
    def __init__(self, title, resizable, validation):
        JPT_RUN_CODE("from pyjdg import *")
        message = "dlg=JDGCreator(title='{}',resizable={},validation={})".format(title, resizable, validation)
        JPT_RUN_CODE(message)

