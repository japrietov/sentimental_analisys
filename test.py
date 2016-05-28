# -*- coding: utf-8 -*-
__author__ = 'japrietov'

import re

import sys  # sys.setdefaultencoding is cancelled by site.py

reload(sys)  # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding("utf-8")
"""
# lematizador R
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

STAP = SignatureTranslatedAnonymousPackage
with open('lematizador.r', 'r') as f:
    string = f.read()

# Funciones del lematizador quedan guardados, su llamado es myfunc.metodo.
myfunc = STAP(string, "lematizador")


data = "Todo lo ?????que empieza mal @¿?¿¿¿¿¿¿+´''''''EnriquePenalosa termina mal http://www.kienyke.com/kien-escribe/penalosa-empezo-mal/yo"

data = (re.sub(u'[^\wáéíóúñ#@\n\t\s((:][=/*>-}{|ü]', '', u''+data))

data = data.replace('¿', '')
data = data.replace('\'', '')


for i in data.split():
    if not urlparse(i).scheme:
        print(i)
print(data)


def cleaned_emotions(emotions):
    cleaned = set()
    for i in emotions:
        emotion_cleaned = str(myfunc.lematizador(i)[0])
        if emotion_cleaned == 'NA':
            cleaned.add(i)
        else:
            cleaned.add(emotion_cleaned)
    return cleaned

negative = open("pspa.txt")
negative_list = negative.read().strip().split()

tmp = cleaned_emotions(negative_list)

for i in tmp:
    print(i)
"""
from Tkinter import *

def saludar():
    print 'Hola'

w = Tk()

l = Label(w, text='Hola progra')
l.pack()

b1 = Button(w, text='Saludar', command=saludar)
b1.pack()

b2 = Button(w, text='Salir', command=exit)
b2.pack()

w.mainloop()