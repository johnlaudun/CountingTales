#! /usr/bin/env python

import glob
import re
import nltk

files = {}
for fpath in glob.glob("*.txt"):
    with open(fpath) as f:
         fixed_text = re.sub("[^a-zA-Z'-]"," ",f.read())
    words = fixed_text.split()
    total_words = len(words)
    total_unique = len(set(words))
    tokens = nltk.wordpunct_tokenize(fixed_text)
    lemmas = [nltk.WordNetLemmatizer.lemmatize(t) for t in tokens]
    t_count = len(tokens)
    l_count = len(lemmas)
    
    files[fpath] = (total_words, total_unique, t_count, l_count)

with open("file_counts.csv", "w") as f:
    for fname in files:
        print >> f, "%s,%s,%s" % (fname, files[fname][0],files[fname][1],files[fname][2],files[fname][3])