# Eulers Method

def eulers(f, x0, y0, value_of_x, h):
  x = x0
  y = y0
  fun = f(x0, y0)

  while x < value_of_x:
      y += h * fun
      x += h
      fun = f(x, y)

  return y

def f(x, y):
    return (y-x)/(y+x)

x0 = float(input("Enter the value of x0: "))
y0 = float(input("Enter the value of y0: "))
value_of_x = float(input("Enter the value of target x: "))
h = float(input("Enter the value of h: "))

print("Value of y at x = ", value_of_x, "is: ", eulers(f, x0, y0, value_of_x, h))
