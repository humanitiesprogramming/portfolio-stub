# count and analyze birth_dates in a dictionary


birth_nm_dates = {
    'Wallace Stevens': 1880,
    'Gertrude Stein': 1880,
    'Charles Bernstein':1950,
    'Emily Dickinson':1830,
    'Ralph Waldo Emerson':1803,
    'Henry Wordsworth Longfellow':1807,
    'Henry David Thoreau':1817,
    'Walt Whitman':1819,
    'Robert Frost':1874}


# print("----Giving simple list---- \n")
# for name, date in birth_nm_dates.items():
#    print (name,date)

#print("----Testing List---- \n")

# counter beginning here


def count_it():
    nnth = 0
    twth = 0
    tot_auth = 0

    for name, date in birth_nm_dates.items():
        if date < 1900:
            nnth = nnth + 1
        else:
            twth = twth +1
        tot_auth = tot_auth + 1
#        tot_auth = 20


    print(f'''
    You have {nnth} nineteenth century
    and {twth} twentieth century authors.

    You have a total of {tot_auth} authors.''')

# just modularizing by putting it all in a function
count_it()
