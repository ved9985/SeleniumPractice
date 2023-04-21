x=5
y=0

try:
    print(x/y)
except Exception as e:
    print("Something went wrong:", e)
except ZeroDivisionError as e:
    print("We can not divide by zero :", e)

finally:
    print("finally done")