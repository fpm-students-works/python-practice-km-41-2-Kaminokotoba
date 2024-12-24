def fact(n):
    if n < 0:
     raise ValueError("Має бути додатнє число")
    if n == 0 or n == 1:
     return 1
    return n * fact(n - 1)