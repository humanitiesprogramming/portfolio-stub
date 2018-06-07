# creating a list and using a method to print it


names = ['Charles Dickens','William Thackery','Anthony Trollope','Gerard Manley Hopkins']

dates = [1870,1863,1882,1889]

def epitaphs(nm,dt):
    print(f"{nm} kicked the bucket in {dt}")

epitaphs(names[1],dates[1])

##### ERROR This prints name twice

# for i in names:
#    epitaphs(i,dates[i])
#    epitaphs(i,i)

##### Error this prints just 1, 2, 3 in variables

# for i in range(1,len(names)):
#    epitaphs(i,i)

counter = 0
while counter < len(names):
    epitaphs(names[counter],dates[counter])
    counter = counter + 1
