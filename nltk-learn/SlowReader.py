import nltk, re, pprint
# from nltk import work_tokenize # unclear if necessary


# READ FILE
def open_file_and_get_text(filename):
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text  # takes the file, reads it. stores it as a string

our_file = "walden.txt"
text = open_file_and_get_text(our_file)
w_words = nltk.word_tokenize(text)
# w_words is now a list
print("These are words")
print(w_words[0:30]) # prints first 29 items in List
nltk_walden_text = nltk.Text(w_words)
print(nltk_walden_text.concordance("the"))

# TOKENIZE file

# FORM SENTENCES - group tokens into list of sentence strings

# SUB SELECT - form a list of sentences incl. "word-x"

# DISPLAYER - increment through the subselect, on sentence at a Time
