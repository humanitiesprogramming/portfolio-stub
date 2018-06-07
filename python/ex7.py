# list pratice subtracting using append
start_list = [10,20,30,40,50]

# creates a blank list
data = []

for i in start_list:
    data.append(i-10)
print("data is now",data)

# This is a shortcut way of iterating through an append sequence in one line!

# short_data = []
short_data = [item +5 for item in data]
print("short data is ", short_data)
