# cascading IF STATEMENTS. Using list and elif


fruits = ["tomato","kiwi", "apple","banana","strawberry"]

print(fruits)

if fruits[0] == 'apple':
    print("Yum")
elif fruits[0] == 'cardboard' or fruits[0] == 'sand':
    print("Yuck")
else:
        print("Not any of those. Is it really a fruit")
