class dob(Exception):
    pass
try:
    year = int(input("Enter the birth year: "))
    age = 2023 - year
    print(age)
    if age<=30 & age>20:
        print("Candidate have valid age")
    else:
        raise dob
except dob:
    print("over age")
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("---------Form end here----")