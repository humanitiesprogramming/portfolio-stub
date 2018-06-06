birth_dates={"Sam Shepard": 1943,
"Tennessee Williams": 1911,
"Arthur Miller": 1915,
"August Strindberg": 1849,
"Henrik Ibsen": 1828}

nineteenth_count=0
twentieth_count=0

for playwrights, years in birth_dates.items():
    if years<1900:
        nineteenth_count=nineteenth_count+1
    elif years>=1900 and years<2000:
        twentieth_count=twentieth_count+1

print("There are " + str(nineteenth_count) + " 19C births and " + str(twentieth_count) + " 20C births in my collection.")
