import math
def root2(x):
    if x < 0:
     raise ValueError("Під квадратним коренем не може бути від'ємне число")
    return math.sqrt(x)
def root3(x):
    return x ** (1/3)