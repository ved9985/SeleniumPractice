lst = [10, 11, 12,10 ,10, 13, 15, 14,-5]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]= lst[j],lst[i]
print(lst)

l1=["a","b","c","d"]
l2=[12,2,3,4]
x= {l1[i]:l2[i] for i in range(len(l1))}
print(x)
dict = {}
for key in l1:
    for value in l2:
        dict[key] = value
print(dict)

