# coding=UTF-8
import collections
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier, MaxentClassifier, SklearnClassifier
import csv
from sklearn import cross_validation
from sklearn.svm import LinearSVC, SVC
import random
from nltk.corpus import stopwords
import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import *
from scipy.sparse import coo_matrix
import numpy as np
from nltk.metrics import scores

posdata = []
with open('./dadostreino/train_EPTC_POA_v3nbal_1.data', 'rb') as myfile:    
    reader = csv.reader(myfile, delimiter=',')
    for val in reader:
        posdata.append(val[0])        
negdata = []
with open('./dadostreino/train_EPTC_POA_v3nbal_0.data', 'rb') as myfile:    
    reader = csv.reader(myfile, delimiter=',')
    for val in reader:
        negdata.append(val[0])            

neudata = []
with open('./dadostreino/train_EPTC_POA_v3nbal_2.data', 'rb') as myfile:    
    reader = csv.reader(myfile, delimiter=',')
    for val in reader:
        neudata.append(val[0])

def word_split(data):    
    data_new = []
    for word in data:
        word_filter = [i.lower() for i in word.split()]
        data_new.append(word_filter)
    return data_new

def word_feats(words):    
    return dict([(word, words.count(word)) for word in words])
    
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out    
    
def gettrainfeat(l, n):
	out = []
	for c in range(0,len(l)-1):
		if (c != n): 
			out = out + l[c]     
 	return out
 	

def treina_classificadores(featx): 	       
    negfeats = [(featx(f), 'neg') for f in word_split(negdata)]
    posfeats = [(featx(f), 'pos') for f in word_split(posdata)]
    neufeats = [(featx(f), 'neu') for f in word_split(neudata)]         
    training_this_round = negfeats + posfeats + neufeats
    classifierME = MaxentClassifier.train(training_this_round, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 1)
    classifierSVM = SklearnClassifier(LinearSVC(), sparse=False)
    classifierSVM.train(training_this_round)
    classifierNB = NaiveBayesClassifier.train(training_this_round)
    feats= featx("18h08 - Incêndio na Av. Borges de Medeiros B/C. Bombeiros e EPTC no local. Via bloqueada, trânsito sendo desviado pela Loureiro da Silva.")
    observed = classifierSVM.classify(feats)
    print observed
 	
treina_classificadores(word_feats)