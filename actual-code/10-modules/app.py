"""
A test main application
"""

import utils  # as u
import calendar

calendar.TextCalendar().prmonth(2025, 3)
# import numpy as np
from utils import printer as p, default_shape
# from utils import *   # possible but not advisable!


class Shape:
    pass

shape = utils.Shape("rhombus")  # namespaced utils/functions/classes
print(shape)
utils.printer(shape)

p("Hello")
p(default_shape)


print(utils.__name__)
print(__name__)
print(utils.__doc__)   # access the docstring
print(__doc__)
print(utils.__file__)  # absolute of the module
print(__file__)

utils._private_function()  # hint at privacy!

from utils import Shape, default_shape, _private_function
from utils import *  # it will ignore anything that has _


utils.Shape("rhombus")
utils.default_shape

import random

print(random.randint(1,10))
print(random.choice(["Alice", "Bob", "Carol"]))

import os

print(os.environ)
print(os.getcwd())
