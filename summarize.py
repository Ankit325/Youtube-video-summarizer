import nltk
import re
from nltk.corpus import stopwords
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import numpy as np
from numpy import *
#nltk.download('punkt')
def summary(subtitle):
    sentences = sent_tokenize(subtitle)
    #print(sentences)
    organized_sent = {k:v for v,k in enumerate(sentences)}
    tf_idf = TfidfVectorizer(min_df=2, 
                                    strip_accents='unicode',
                                    max_features=None,
                                    lowercase = True,
                                    token_pattern=r'w{1,}',
                                    ngram_range=(1, 3), 
                                    use_idf=1,
                                    smooth_idf=1,
                                    sublinear_tf=1,
                                    stop_words = 'english')
    sentence_vectors = tf_idf.fit_transform(sentences)
    sent_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
    N = 3
    top_n_sentences = [sentences[index] for index in np.argsort(sent_scores, axis=0)[::-1][:N]]
    # mapping the scored sentences with their indexes as in the subtitle
    mapped_sentences = [(sentence,organized_sent[sentence]) for sentence in top_n_sentences]
    # Ordering the top-n sentences in their original order
    mapped_sentences = sorted(mapped_sentences, key = lambda x: x[1])
    ordered_sentences = [element[0] for element in mapped_sentences]
    # joining the ordered sentence
    summ = " ".join(ordered_sentences)
    #print(summ)
    return summ

