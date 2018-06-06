year=2000
if year<1900:
    print("Hello ancient human!")
elif year>=1900 and year<=2020:
    print("Hello fellow human!")
else:
    print("Hello future human!")



def say_hello(year):
    if year<1900:
        print("Hello ancient human!")
    elif year>=1900 and year<=2020:
        print("Hello fellow human!")
    else:
        print("Hello future human!")

say_hello(2000)
