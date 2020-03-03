import string
from os import listdir
from nltk.corpus import stopwords
from collections import Counter
#Generating dataset and data-preprocessing
# https://machinelearningmastery.com/prepare-movie-review-data-sentiment-analysis/
#1. Movie Review Dataset
#C:\Users\ADMIN\Desktop\Twitter Sentiment Analysis\Collecting datasets for reviews\txt_sentoken

# 2. Load Text Data
# load one file
filename = r'C:\Users\ADMIN\Desktop\Twitter Sentiment Analysis\Collecting datasets for reviews\txt_sentoken\neg\cv000_29416.txt'
# open the file as read only
file = open(filename, 'r')
# read all text
text = file.read()
# close the file
file.close()

# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text


from os import listdir


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

#This will load the file name
# specify directory to load
directory = r'C:\Users\ADMIN\Desktop\Twitter Sentiment Analysis\Collecting datasets for reviews\txt_sentoken\neg'
# walk through all files in the folder
for filename in listdir(directory):
    # skip files that do not have the right extension
    if not filename.endswith(".txt"):
        continue
    # create the full path of the file to open
    path = directory + '/' + filename
    # load document
    doc = load_doc(path)
    print('Loaded %s' % filename)

#3. Cleaning of data
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# load the document
filename = r'C:\Users\ADMIN\Desktop\Twitter Sentiment Analysis\Collecting datasets for reviews\txt_sentoken\neg\cv000_29416.txt'
text = load_doc(filename)
# split into tokens by white space
tokens = text.split()
# remove punctuation from each token
table = str.maketrans('', '', string.punctuation)
tokens = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
tokens = [word for word in tokens if word.isalpha()]
# filter out stop words
stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words]
# filter out short tokens
tokens = [word for word in tokens if len(word) > 1]
print(tokens)
#
# #4. Develop Vocabulary
# #Below is a function called add_doc_to_vocab() that takes as arguments a document filename and a Counter vocabulary.
# # load doc and add to vocab
# def add_doc_to_vocab(filename, vocab):
#     # load doc
#     doc = load_doc(filename)
#     # clean doc
#     tokens = clean_doc(doc)
#     # update counts
#     vocab.update(tokens)
#
#
# # load all docs in a directory
# def process_docs(directory, vocab):
#     # walk through all files in the folder
#     for filename in listdir(directory):
#         # skip files that do not have the right extension
#         if not filename.endswith(".txt"):
#             continue
#         # create the full path of the file to open
#         path = directory + '/' + filename
#         # add doc to vocab
#         add_doc_to_vocab(path, vocab)
#
#
# # save list to file
# def save_list(lines, filename):
#     data = '\n'.join(lines)
#     file = open(filename, 'w')
#     file.write(data)
#     file.close()
#
#
# # define vocab
# vocab = Counter()
# # add all docs to vocab
# process_docs(r'C:\Users\ADMIN\Desktop\Twitter Sentiment Analysis\Collecting datasets for reviews\txt_sentoken\neg', vocab)
# process_docs(r'C:\Users\ADMIN\Desktop\Twitter Sentiment Analysis\Collecting datasets for reviews\txt_sentoken\pos', vocab)
# # print the size of the vocab
# print(len(vocab))
# # print the top words in the vocab
# print(vocab.most_common(50))
# # keep tokens with > 5 occurrence
# min_occurane = 5
# tokens = [k for k, c in vocab.items() if c >= min_occurane]
# print(len(tokens))
# # save tokens to a vocabulary file
# save_list(tokens, 'vocab.txt')