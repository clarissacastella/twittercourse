# coding=UTF-8
from nltk.classify import NaiveBayesClassifier, MaxentClassifier, SklearnClassifier
import csv
from sklearn.svm import LinearSVC

def divide(dados):    
    dados_new = []
    for palavra in dados:
        palavra_filter = [i.lower() for i in palavra.split()]
        dados_new.append(palavra_filter)
    return dados_new[0]

def bag_of_words(palavras):    
    return dict([(palavra, palavras.count(palavra)) for palavra in palavras])
    
    
def treina_classificadores():
    posdados = []
    with open('./dadostreino/train_EPTC_POA_v3nbal_1.data', 'rb') as myfile:    
        reader = csv.reader(myfile, delimiter=',')
        for val in reader:
            posdados.append(val[0])               
    negdados = []
    with open('./dadostreino/train_EPTC_POA_v3nbal_0.data', 'rb') as myfile:    
        reader = csv.reader(myfile, delimiter=',')
        for val in reader:
            negdados.append(val[0])                   
    neudados = []
    with open('./dadostreino/train_EPTC_POA_v3nbal_2.data', 'rb') as myfile:    
        reader = csv.reader(myfile, delimiter=',')
        for val in reader:
            neudados.append(val[0])                         
    negfeats = [(bag_of_words(f), 'neg') for f in divide(negdados)]
    posfeats = [(bag_of_words(f), 'pos') for f in divide(posdados)]
    neufeats = [(bag_of_words(f), 'neu') for f in divide(neudados)]
    treino = negfeats + posfeats+ neufeats
    #'Maximum Entropy'
    classificadorME = MaxentClassifier.train(treino, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 1)
    #SVM
    classificadorSVM = SklearnClassifier(LinearSVC(), sparse=False)
    classificadorSVM.train(treino)
    # Naive Bayes
    classificadorNB = NaiveBayesClassifier.train(treino)
    return ([classificadorME,classificadorSVM,classificadorNB])
        
def classifica(sentencas, classificadores):
    ret = []                        
    for s in sentencas:
        c = divide([s])
        feats= bag_of_words(c[0])
        classificacao = []
        classificacao.append(classificadores[1].classify(feats))
        classificacao.append(classificadores[2].classify(feats))
        classificacao.append(classificadores[0].classify(feats))
        ret.append(classificacao)
    return ret

######## MAIN                    	
classificadores = treina_classificadores()

sentences = ['Fluxo muito congestionado na Osvaldo Aranha no acesso para o Túnel. Agora, tá chovendo também. Então, atenção!', \
            'Não use o celular ao volante, 80% da sua atenção é desviada.']

print sentences            
print classifica(sentences, classificadores)
