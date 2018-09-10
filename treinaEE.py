#!/usr/bin/env python
# coding: utf8

from __future__ import unicode_literals
import plac
import random
from pathlib import Path
import spacy

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

dir = "./modeloEE"   # cria modelo em branco
dir = Path(dir)
nlp = spacy.blank('pt')  
dir.mkdir()       	
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner, last=True)
    
import dados_treino as tr
dados_treino = tr.cria_dados_treino('./data/testP.txt') # dados de treino

for _, annotations in dados_treino:
	for ent in annotations.get('entities'):
		ner.add_label(ent[2])

# treina EE
optimizer = nlp.begin_training()
n_iter = 2 #nro iteracoes
for itn in range(n_iter):
    c = 0
    losses = {}        
    for text, annotations in dados_treino:
        c = c + 1
        nlp.update(
            [unicode(text)],  # batch de textos
            [annotations],  # batch de anotacoes
            drop=0.25,
            sgd=optimizer,
            losses=losses)
    print(losses)

nlp.to_disk(dir) #salva modelo

