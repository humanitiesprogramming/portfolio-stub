list=[1,2,3,4,5]
data=[]
for x in list:
    data.append(x-10)

print(data)
data=[x-10 for x in list]
print(data)
