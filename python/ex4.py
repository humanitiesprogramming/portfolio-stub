# Practive from Python programming for humanists
# working with lists and dictionaries
#

# first example, a dictionary because {}

my_info = {
    'fname': 'Ken',
    'lname': 'Sherwood',
    'hometown': 'Indiana',
    'ppn':"his",
    'fav_food':'paella'}
print("This is the my_info dict")
print(my_info)
print("This is the first item")
print(my_info['fname'])
my_info['fname'] = 'Kenny'

# Pratice replacing an item in the dictionary
print("this is another variant of the name",
my_info['fname'])


# THIS is the example of a list, which can move through items numerically.


my_name_var = ['Ken','Kenn','Kenny','Kenneth','Kent','Kencito']
print('A list of name variants: \n')
print(my_name_var)

# This loops through and prints one for each line.

for n in my_name_var:
    print('\n')
    print(f'This is a variant: {n}')
    print('\n')
