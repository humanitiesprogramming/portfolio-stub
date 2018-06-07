# THIS ITERATES THROUGH THE PAIR OF A dictionary using ".item"
# SO.  Effecxtively ".items" turns a dictionary into a sequential list so that you can move through the items in order.

states_names ={"VA":"Virginia","MD":"Maryland"}

for abbrev, state in states_names.items():
  print(abbrev+ " is the code for " + state)
