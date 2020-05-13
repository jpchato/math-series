def fibonacci(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  if n == 0:
    return 2
  if n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)