# -*- coding: utf-8 -*-
__author__ = 'japrietov'

import csv
import re
from nltk.corpus import stopwords
import sys  # sys.setdefaultencoding is cancelled by site.py
import string
reload(sys)  # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding("ISO-8859-1")
from urlparse import urlparse

# lematizador R
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

STAP = SignatureTranslatedAnonymousPackage
with open('lematizador.r', 'r') as f:
    string = f.read()

# Funciones del lematizador quedan guardados, su llamado es myfunc.metodo.
myfunc = STAP(string, "lematizador")

data_twitter = []
clean_data_text = []

with open('output_test.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for i in spamreader:
        data_twitter.append(i)

for data in data_twitter:
    clean_data_text.append(data[4].encode("utf-8"))

data_analisys = []

positive = open("positive_words_cleaned.txt")
positive_list = set(positive.read().split())

negative = open("negative_words_cleaned.txt")
negative_list = set(negative.read().split())


for row in clean_data_text:

    # data = (re.sub(r'[^\wáéíóúñ#@\n\t\s]','',row))

    data = row

    # Save all information in a list, for saving in a .json file

    # lematizado de las palabras.
    important_word = []
    for word in data.split():
        if word not in stopwords.words('spanish') and word not in list("áéíóúüabcdefghijklmnopqrstuvwxyz") \
                and not word.isdigit() and not urlparse(word).scheme and "pic.twitter" not in word:
            important_word.append(word)

    #data = " ".join(important_word)

    lematizada = []
    changeWord = []
    for i in important_word:
        if "@" in i:
            continue
        else:
            asd = str(myfunc.lematizador(i)[0])
            if asd == 'NA':
                lematizada.append(i)
                changeWord.append('0')
            else:
                lematizada.append(asd)
                changeWord.append('1')

    data = " ".join(lematizada)
    data = (re.sub(u'[^\wáéíóúñ#@\n\t\s((:][=/*>-}{|ü]', '', u''+data))
    data = data.replace('¿', '')
    data = data.replace('?', '')
    data = data.replace('\'', '')

    tmp = []

    for item in range(len(lematizada)):
        tmp.append(lematizada[item])
        tmp.append(changeWord[item])
        tmp.append(',')


    tmp = data.split()

    for emotion_positive in positive_list:
        for value in tmp:
            if emotion_positive in value:



#    tmp.pop()
    """
    tmp = " ".join(tmp)
    print "Palabras sin preprocesar: ", row
    print "Palabras preprocesadas: ",data.encode('ISO-8859-1')
    print
    """
    #data_analisys.append(" ".join(data_list))
    print(" ".join(tmp))



#print(data_analisys)

data_positive_negative = {}
for data_key in data_analisys:
    data_key_set = set(data_key.split())
    data_positive_negative[data_key] = [len(data_key_set.intersection(positive_list)),len(data_key_set.intersection(negative_list))]


for k in data_positive_negative:
    tmp = str(k).encode("ISO-8859-1")
    print(tmp)
    print(data_positive_negative[k][0], data_positive_negative[k][1])



# Save .jason file
# with open('cleaned_twitter.json', 'w') as f:
#   json.dump(clean_data_twitter, f)
