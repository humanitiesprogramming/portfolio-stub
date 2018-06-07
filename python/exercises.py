greeting = input("Hello, possible pirate! What's the password?")
if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print(str(author) + " died in " + str(date) + ".")

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")

# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

classy Person:
  def __initalize__(self, first_name, last_name):
    self.first = first_name
    self.last = lname
  def speak(self):
  print("My name is + " self.fname + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.self.speak
