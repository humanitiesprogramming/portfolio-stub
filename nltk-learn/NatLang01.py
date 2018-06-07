from bs4 import BeautifulSoup
from urllib import request
import nltk
############### modifying tutorial from:https://humanitiesprogramming.github.io/resources/
############### These lines omitted so as to work on local version
#url = "https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/full-text.txt"
#html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'lxml')

def open_file_and_get_text(filename):       # given a filename, openit
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text

our_file = "source.txt" # local source text
text = open_file_and_get_text(our_file)

# ?????
soup = text

raw_text = soup.text
texts = eval(soup.text)
print(len(raw_text))
print(len(texts))
