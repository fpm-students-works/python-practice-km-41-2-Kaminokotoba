import math

def log(a, b):
    if a <= 0 or a == 1:
     raise ValueError("число a має бути більше за 0 та не дорівнює 1")
    if b <= 0:
     raise ValueError("число b має бути більше за 0")
    return math.log(b, a)

def ln(b):
    if b <= 0:
     raise ValueError("число b має бути більше за 0")
    return math.log(b)

def lg(b):
    if b <= 0:
     raise ValueError("число b має бути більше за 0")
    return math.log10(b)