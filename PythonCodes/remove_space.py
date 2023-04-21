s = "I am Present"
result= ""
ch= ""
for i in s:
    if i==" ":
        i=ch
    result = result + i
print(result)


v=""
for j in s:
    if j in ['a','e' ,'i', 'o', 'u']:
        j=""
    v=v+j
print(v)