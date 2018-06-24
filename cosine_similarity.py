import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_similarity_score
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

def calculate_cosine_similarity(documents) :

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    #print "Array:"
    #print tfidf_matrix.toarray()

    print "Matrix:"
    print tfidf_matrix
    print cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    #print tfidf_vectorizer.get_feature_names()

    #print "Test"
    #print tfidf_vectorizer.get_feature_names()

    print "Cosine Pairwise:"
    print 1 - pairwise_distances(tfidf_matrix, metric='cosine')


def calculate_jaccard_similarity(documents):

    print "not possible"
    #The Jaccard similarity does not work in continuous values


    # tfidf_vectorizer = TfidfVectorizer()
    # tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    #
    # print "Test matrix"
    # print tfidf_matrix.shape
    # tfidf_array = tfidf_matrix.toarray()
    # print "Jaccard Similarity"
    # print tfidf_array[0]
    # print tfidf_array[1]
    # jaccard_similarity_score(tfidf_array[0], tfidf_array[1])


def calculate_euclidean_similarity(documents):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    print pairwise_distances(tfidf_matrix, metric='euclidean')