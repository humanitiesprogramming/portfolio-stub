# import the modules that we need
# use Beautiful Soup to scrape down the corpus
# eval() function tells Python to take a string it is passed and interpret it as code
# Beautiful Soup pulls down the contents of a website, but it assumes that the result of soup.text is going to be a string. If you actually look at the contents of that link, though, you'll see that I dumped the contents of the texts as a list of texts. So we need to interpret that big long text file as code, and Python can help us do that. Calling eval on it looks for special characters like the [], which indicate lists, and runs Python on it as expected. To actually work with this code again.

from bs4 import BeautifulSoup
from urllib import request

url = "https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/full-text.txt"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
texts = eval(soup.text)

# taking the length of our two different versions of the soup results
# The first len() function is way larger, as it is taking the length of a giant string. So it returns the total number of characters in the collected text. The second statement gives us the expected result "10", because it is measuring the length of our list of texts. We have 10 of them. As always, it is important that we remember what data types we have and when we have them.

# print(len(raw_text))
# print(len(texts))

# Now that we have our data, we can start processing it as text. The package we are using is NLTK, the Natural Language Toolkit, which is something of a Swiss army knife for text analysis.

import nltk
from nltk import word_tokenize

# Before we get going, we'll have to load in some additional nltk data. Fire this up from within the interpreter (you'll have to import nltk first)

# nltk.download()

# The first step in our process is to break the text into smaller units that we can work with. In any tokenization process, you have to decide what kinds of things count as tokens - does punctuation count? How do we deal with word boundaries? You could tokenize things yourself, but it's not necessary to reinvent the wheel. We'll use NLTK to tokenize for us.

tokenized_texts = []
for text in texts:
    tokenized_texts.append(word_tokenize(text))

# for tokenized_text in tokenized_texts:
    # print('=====')
    # print(len(tokenized_text))
    # print(tokenized_text[0:20])

# We've got a series of texts, all of which are tokenized. But wow those are big numbers. Lots of words! Five texts by Charlotte Bronte and five by Sir Arthur Conan Doyle. Let's get a little more organized by separating the two corpora by author

doyle = tokenized_texts[:5]
bronte = tokenized_texts[5:]

# print(len(doyle))
# print(len(bronte))

# lowercase all words (for a computer, "The" is a different word from "the")
# remove the Project Gutenberg frontmatter (you may have noticed that all the texts above started the same way)
# For the second one, Project Gutenberg actually makes things a little tricky. Their frontmatter is not consistent from text to text. We can grab nine of our texts by using the following phrases: "START OF THIS PROJECT GUTENBERG EBOOK." This won't perfectly massage out all the frontmatter, but for the sake of simplicity I will leave it as is. For the sake of practice, we'll be defining a function for doing these things.

def normalize(tokens):
    """Takes a list of tokens and returns a list of tokens
    that has been normalized by lowercasing all tokens and
    removing Project Gutenberg frontmatter."""

#     lowercase all words
    normalized = [token.lower() for token in tokens]

#     very rough end of front matter.
    end_of_front_matter = 90
#     very rough beginning of end matter.
    start_of_end_matter = -2973
#     get only the text between the end matter and front matter
    normalized = normalized[end_of_front_matter:start_of_end_matter]

    return normalized

# print(normalize(bronte[0])[:200])
# print(normalize(bronte[0])[-200:])

# Go through each in the list of texts
# For each of those texts, normalize the text in them using the function we defined above.
# Take the results of that normalization process and make a new list out of them.
# The result will be a list of normalized tokens stored in a variable of the same name as the original list.

doyle = [normalize(text) for text in doyle]
bronte = [normalize(text) for text in bronte]

# print(doyle[0][:30])

# The last step in this basic text analysis pipeline is to remove those words that we don't care about. The most common words in any text are articles, pronouns, and punctuation, words that might not carry a lot of information in them about the text themselves. While there are sometimes good reasons for keeping this list of stopwords in the text, we usually take them out to get a better read of things we actually care about in a text. NLTK actually comes with a big packet of stopwords. Let's import it:

from nltk.corpus import stopwords

# print(stopwords.words('english')[0:30])

# We'll loop over the cleaned texts and get rid of those words that exist in the stopwords list. To do this, we'll compare both lists.
# Also grab the count for the text pre-stopwording to make clear how many words are lost when you do this:

def remove_stopwords(tokens):
    return [token for token in tokens if token not in stopwords.words('english')]

# We could loop over each text again, as we have been doing:

# print(len(doyle[0]))
# print('start cleaning')
doyle = [remove_stopwords(text) for text in doyle]
# print('doyle done')
bronte = [remove_stopwords(text) for text in bronte]
# print('bronte done')

# print(len(doyle[0]))

# One thing we can do quite easily is count up the frequencies with which particular words occur in a text. NLTK has a particular way of doing this using an object called a Frequency Distribution, which is exactly what it sounds like. We make a frequency distribution of a text like so:

example = nltk.FreqDist(doyle[0])
# print(example.most_common(30))

# Above, we take the first Doyle text, make a Frequency Distribution out of it, and store it in a variable called example. We can then do frequency distribution things with it, like find the most common words! Let's do this for all our texts:

doyle_freq_dist = [nltk.FreqDist(text) for text in doyle]
bronte_freq_dist = [nltk.FreqDist(text) for text in bronte]

def print_top_words(freq_dist_text):
    """Takes a frequency distribution of a text and prints out the top 10 words in it."""
    print('=====')
    print(freq_dist_text.most_common(10))
    print('=====')

# for text in doyle_freq_dist:
    # print_top_words(text)
# for text in bronte_freq_dist:
    # print_top_words(text)

# We can also query particular words:

# print(doyle_freq_dist[0]['holmes'])
# print(bronte_freq_dist[0]['would'])

# Let's make a quick function that would, given a particular word, return the frequencies of that word in both corpora.

def get_counts_in_corpora(token, corpus_one, corpus_two):
    """Take two corpora, represented as lists of frequency distributions, and token query.
    Return the frequency of that token in all the texts in the corpus. The result
    Should be a list of two lists, one for each text."""
    corpus_one_counts = [text_freq_dist[token] for text_freq_dist in corpus_one]
    corpus_two_counts = [text_freq_dist[token] for text_freq_dist in corpus_two]
    return  [corpus_one_counts, corpus_two_counts]

# print(get_counts_in_corpora('evidence', doyle_freq_dist, bronte_freq_dist))
# print(get_counts_in_corpora('reader', doyle_freq_dist, bronte_freq_dist))
# print(get_counts_in_corpora('!', doyle_freq_dist, bronte_freq_dist))
# print(get_counts_in_corpora('?', doyle_freq_dist, bronte_freq_dist))

# We now have an easy way to get the total counts for any word, and we could get one corpus or the other by slicing the one list out:

results = get_counts_in_corpora('!', doyle_freq_dist, bronte_freq_dist)
corpus_one_results = results[0]
corpus_two_results = results[1]

# print(corpus_one_results)
# print(corpus_two_results)

# A dispersion plot gives you a rough indication of the word usage in a particular text, and it has the added benefit of showing where particular usages cluster. You can pass a list of terms to it.

# nltk.Text(doyle[0]).dispersion_plot(['evidence', 'clue', 'science', 'love', 'say', 'said'])
# nltk.Text(bronte[0]).dispersion_plot(['evidence', 'clue', 'science', 'love', 'say', 'said'])

dear_results = get_counts_in_corpora("dear", doyle_freq_dist, bronte_freq_dist)
dear_corpus_one_results = dear_results[0]
dear_corpus_two_results = dear_results[1]

# print("Frequency of Dear in Doyle")
# print(dear_corpus_one_results)
# print("Frequency of Dear in Bronte")
# print(dear_corpus_two_results)
