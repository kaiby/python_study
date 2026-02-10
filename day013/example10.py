"""
example10 - 

Author: kaiby
Date: 2024/1/10 15:39
"""
from enum import Enum


class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)


for suite in Suite:
    print(suite.name, suite.value)
