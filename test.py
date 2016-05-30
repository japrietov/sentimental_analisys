# -*- coding: utf-8 -*-
import codecs

__author__ = 'japrietov'

import re
import sys  # sys.setdefaultencoding is cancelled by site.py
import csv
from nltk.corpus import stopwords
"""
for data in data_twitter:
    clean_data_text.append(data[4].encode("utf-8"))


negative = open("negative_words_cleaned.txt")
negative_list = negative.readlines()

from itertools import izip_longest

positive = open("positive_words_cleaned.txt")
positive_list = positive.readlines()

positive_dict = {}
negative_dict = {}

for j in positive_list:
    tmp = j.split()
    positive_dict[tmp[0]] = int(tmp[1])


for j in negative_list:
    tmp = j.split()
    print(tmp)
    negative_dict[tmp[0].strip()] = int(tmp[1])


print(negative_dict)
print(len(negative_list))





data = "@HSBnoticias @Prensa_Alcaldia @EnriquePenalosa esto no era lo que uds llamaban \"populismo\". A partir de hoy se llama Institucionalidad."


positive_sentiments = 0

# lematizador R
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

STAP = SignatureTranslatedAnonymousPackage
with open('lematizador.r', 'r') as f:
    string = f.read()

# Funciones del lematizador quedan guardados, su llamado es myfunc.metodo.
myfunc = STAP(string, "lematizador")


lematizada = []
for i in data.split():
    if "@" in i or i in stopwords.words('spanish'):
        continue
    else:
        asd = str(myfunc.lematizador(i)[0])
        if asd == 'NA':
            lematizada.append(i)
        else:
            lematizada.append(asd)

data = " ".join(lematizada)
data = (re.sub(u'[^\wáéíóúñ#@\n\t\s((:][=/*>-}{|ü]', '', u''+data))
data = data.replace('¿', '')
data = data.replace('?', '')
data = data.replace('\'', '')

tmp = data.split()

for emotion_positive in positive_list:
    for value in tmp:
        if value in emotion_positive:
            print (value, emotion_positive)
            positive_sentiments +=1

print(tmp)
print(positive_sentiments)


data = "@GustavoBolivar @freito Y despuÈs dir·n que todo es obra del gran urbanista @EnriquePenalosa. Gran prensa. @ELROLODELA14 @EnriquePenalosa Se nota que ni siquiera pasÛ la primaria. QuÈ verg¸enza expresarse asÌ. Pobre diablo."

stopwords_words = [x.encode('utf-8') for x in stopwords.words('spanish')]


chars = "áéíóúüÑñÁÉÍÓÚÜabcdefghijklmnopqrstuvwxyz"
rare_chars = "ÁÉÍÓÚÜÑ"

list_chars = list(chars) + list(chars.upper())

print(stopwords_words)

for i in data.split():
    if not i.isupper():
        i = i.decode('utf-8').lower()
    if i not in stopwords_words and i not in list_chars:
        print (i)



negative = open("negative_words_cleaned.txt")
negative_list = negative.readlines()

positive = open("positive_words_cleaned.txt")
positive_list = positive.readlines()

positive_dict = {}
negative_dict = {}

for j in positive_list:
    tmp = j.split()
    print(tmp)
    positive_dict[tmp[0]] = int(tmp[1])


for j in negative_list:
    tmp = j.split()
    print(tmp)
    negative_dict[tmp[0].strip()] = int(tmp[1])

"""

string1 = "calvin klein design dress calvin klein"
words = string1.split()
print " ".join(sorted(set(words), key=words.index))