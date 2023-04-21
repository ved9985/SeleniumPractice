x=5
y=0

try:
    print(x/y)
except Exception as e:
    print("ZeroDivisionError:", e)
try:
    print(4 + spam*3)
except Exception as e:
    print("NameError:", e)
try:
    print('2'+2)
except Exception as e:
    print("TypeError:", e)

finally:
    print("finally done")