# coding: utf8
import ast
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def cria_dados_treino(arq='./data/dadosTreinoLoc.txt'):
	dados_treino = []
	fin = open(arq, 'rb')
	n=0
	post = u''
	for val in fin:
		d = {}
		n = n + 1
		if (n % 2 == 1) :
			post = val.replace('\n','')
		else :
			d['entities']=ast.literal_eval(val.replace('\n',''))	
			dados_treino.append((post, d))		
	fin.close()
	return dados_treino
	
