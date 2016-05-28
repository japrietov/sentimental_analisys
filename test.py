# -*- coding: utf-8 -*-
__author__ = 'japrietov'

import re

import sys  # sys.setdefaultencoding is cancelled by site.py
from nltk.corpus import stopwords
reload(sys)  # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding("utf-8")

# lematizador R
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

STAP = SignatureTranslatedAnonymousPackage
with open('lematizador.r', 'r') as f:
    string = f.read()

# Funciones del lematizador quedan guardados, su llamado es myfunc.metodo.
myfunc = STAP(string, "lematizador")


def cleaned_emotions(emotions):
    cleaned = set()

    for i in emotions:
        if i not in stopwords.words('spanish') and i not in list("áéíóúüabcdefghijklmnopqrstuvwxyz"):
            emotion_cleaned = str(myfunc.lematizador(i)[0])
            if emotion_cleaned == 'NA':
                cleaned.add(i)
            else:
                cleaned.add(emotion_cleaned)

    return cleaned

negative = open("nspa.txt")
negative_list = negative.read().strip().split()

tmp = cleaned_emotions(negative_list)

for i in tmp:
    print(i)

"""
negative = open("pspa.txt")
negative_list = set(negative.read().strip().split())

from itertools import izip_longest

positive = open("positive_words_cleaned.txt")
positive_list = set(positive.read().split())

for emotion_negative, emotion_positive in izip_longest(negative_list, positive_list):
    print(emotion_negative, emotion_positive)
"""

