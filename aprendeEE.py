#!/usr/bin/env python
# coding=UTF-8
#from __future__ import unicode_literals
from elasticsearch import Elasticsearch
#import plac
#import random
from pathlib import Path
import spacy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

modelo_dir = Path("./model10iter")
modelo = spacy.load(modelo_dir)  # roda modelo

fin = open('./data/postsP.txt', 'rb')
for text in fin:
        doc_model = modelo(unicode(text))
        locs = []
        for ent in doc_model.ents:
            aux = (ent.start_char, ent.end_char, str(ent.label_))
            locs.append(text[ent.start_char:ent.end_char+1])                
        print text, locs
         
