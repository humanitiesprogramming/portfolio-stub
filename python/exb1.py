# Calling a function within a fucxntion.
# Make a program that counts from ten numbers in sequence


def counting_10(start_num):
    # This counts from a given beginning number and prints out the next 9 in sequence
    for i in range(1,11):
        print(i+start_num)

def assig_init_num(x):
    # This function accepts the first number as an argument and then sends it to the counting_10 method above. It's not really necessary (i.e. the two could be combined) but it shows how it could work.
    counting_10(x)

# program starts here
assig_init_num(20)
