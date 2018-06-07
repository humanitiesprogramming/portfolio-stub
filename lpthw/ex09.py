#printing printing printing ex 9 in Learn Python the Hard Way - adapted

# string not items
days = "Mon Tue Wed Thu Fri Sat Sun"

# incorporating what i know of lists
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

print(f"There are days {days}")

#iteration practice
for n in range(1,10):
    for i in months:
        print(i)

# exploring multiline

print("""
How does this work?
And does it keep the linebreaks?
And why or why not?
""")

# can I create a multiline string
string_test = """
this is one line
this is another
they will print separately
and at least line spacing is
main
        tained
as well as     interior spacing

   _____
       /ZZZZZ)
       |____/
       |ZZZZ|
       \__ ___ \
       |ZZZZZ . ___
     .'(\ @ @)_.
       /;   " )-
       \; `--'
         \,'/
      ___|;|___
     >xXX>O
"""

print(string_test)

str_test = """
space     is
     <pre>       served 
"""
print(str_test)
