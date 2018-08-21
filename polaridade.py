# coding=UTF-8
from nltk.classify import NaiveBayesClassifier, MaxentClassifier, SklearnClassifier
import csv
from sklearn.svm import LinearSVC

def word_split(data):    
    data_new = []
    for word in data:
        word_filter = [i.lower() for i in word.split()]
        data_new.append(word_filter)
    return data_new

def word_feats(words):    
    return dict([(word, words.count(word)) for word in words])

def evaluate_classifier(featx, sentences):
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
        negfeats = [(featx(f), 'neg') for f in word_split(negdata)]
        posfeats = [(featx(f), 'pos') for f in word_split(posdata)]
        neufeats = [(featx(f), 'neu') for f in word_split(neudata)]

        training_this_round = negfeats + posfeats+ neufeats
        #'Maximum Entropy'
        classifierME = MaxentClassifier.train(training_this_round, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 1)
        #SVM
        classifierSVM = SklearnClassifier(LinearSVC(), sparse=False)
        classifierSVM.train(training_this_round)
        # Naive Bayes
        classifierNB = NaiveBayesClassifier.train(training_this_round)
			                        
        for s in sentences:
            c = word_split([s])
            feats= featx(c[0])
            observed = []
            observed.append(classifierSVM.classify(feats))
            observed.append(classifierNB.classify(feats))
            observed.append(classifierME.classify(feats))
            print s, observed
                    	
sentences = ['Queda de poste na Av. Sertório x R. Diamantina. Av Sertório sentido C/B totalmente bloqueada. Agentes da EPTC no local.', \
            'Não há mais manifestações na Est. Afonso Lourenço Mariante. Trânsito fluindo sem problemas.', \
            'Não use o celular ao volante, 80% da sua atenção é desviada.']
evaluate_classifier(word_feats,sentences)