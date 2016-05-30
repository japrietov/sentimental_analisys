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
myfunc_lematizzer = STAP(string, "lematizador")


def open_data():
    data_twitter = []
    clean_data_text = []

    with open('output_got.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for i in spamreader:
            data_twitter.append(i)

    for data in data_twitter:
        clean_data_text.append(data[4].decode("ISO-8859-1"))
        #clean_data_text.append(data[0].split(',')[4    ].encode('utf-8'))


    return clean_data_text


def clean_data(clean_data_text):
    data_complete = []
    changeWord_complete = []

    stopwords_words = [x.encode('utf-8') for x in stopwords.words('spanish')]

    chars = "áéíóúüabcdefghijklmnopqrstuvwxyz"

    list_chars = list(chars) + list(chars.upper())


    for row in clean_data_text:

        data = row.split()

        # Save all information in a list, for saving in a .json file
        # lematizado de las palabras.
        important_word = []
        for word in data:
            if not word.isupper():
                word = word.lower()
            if word not in stopwords_words and word not in list_chars and not word.isdigit() and not urlparse(word).scheme and "pic.twitter" not in word:
                important_word.append(word)

        #data = " ".join(important_word)

        lematizada = []
        changeWord = []

        data = " ".join(important_word)
        data = (re.sub("(\Wáéíóúñ\(\):=/*>-}{|ü)*(0-9],?.'¿\")", "", data))
        data = (re.sub("([0-9],\?.\'\¿\")*", "", data))

        print(data)

        important_word = data.split()

        for i in important_word:
            if "@" not in i:
                asd = str(myfunc_lematizzer.lematizador(i)[0])
                if asd == 'NA':
                    lematizada.append(i)
                    changeWord.append('0')
                else:
                    lematizada.append(asd)
                    changeWord.append('1')

        data_complete.append(lematizada)
        changeWord_complete.append(changeWord)

    return data_complete, changeWord_complete


def import_data_to_RAE(data_complete, changeWord_complete):

    tmp_complete = []
    for data in range(len(data_complete)):
        tmp = []
        lematizada = data_complete[data]
        changeWord = changeWord_complete[data]

        for item in range(len(lematizada)):
            tmp_lematizada = lematizada[item]
            if (len(tmp_lematizada) < 3 and not tmp_lematizada.isalnum()) or len(tmp_lematizada) > 2:
                tmp.append(lematizada[item].encode('utf-8'))
                tmp.append(changeWord[item])
                tmp.append(',')

        tmp_complete.append(" ".join(tmp))

    return tmp_complete

"""

def emotions_twitter():
        data_analisys_dict = {}

        positive_sentiments = 0
        negative_sentiments = 0
        for emotion_positive in positive_list:
            for value in tmp:
                 if value == emotion_positive:
                    positive_sentiments +=1

        data_analisys_dict[data] = positive_sentiments

        print data_analisys_dict

    #data_analisys.append(" ".join(data_list))
    print(" ".join(tmp))


data_analisys = []

positive = open("positive_words_cleaned.txt")
positive_list = set(positive.read().split())

negative = open("negative_words_cleaned.txt")
negative_list = set(negative.read().split())

#print(data_analisys)
data_positive_negative = {}
for data_key in data_analisys:
    data_key_set = set(data_key.split())
    data_positive_negative[data_key] = [len(data_key_set.intersection(positive_list)),len(data_key_set.intersection(negative_list))]


for k in data_positive_negative:
    tmp = str(k).encode("ISO-8859-1")
    print(tmp)
    print(data_positive_negative[k][0], data_positive_negative[k][1])

"""


negative = open("negative_words_cleaned.txt")
negative_list = negative.readlines()


positive = open("positive_words_cleaned.txt")
positive_list = positive.readlines()

positive_dict = {}
negative_dict = {}

for positive_tmp in positive_list:
    tmp_positive = positive_tmp.split()
    positive_dict[tmp_positive[0]] = int(tmp_positive[1])

for negative_tmp in negative_list:
    tmp_negative = negative_tmp.split()
    negative_dict[tmp_negative[0].strip()] = int(tmp_negative[1])

def sentimental_analisys(tweet):
    tmp = tweet.split()
    positive_sentiments = 0
    negative_sentiments = 0
    for value_pos in tmp:
        value_tmp_pos = re.sub('[^a-zA-Z0-9 \n\.]', '', value_pos)
        value_tmp_pos = value_tmp_pos.lower()

        if value_tmp_pos in positive_dict:

            positive_sentiments += positive_dict[value_tmp_pos]
        else:
            if "!" in value_pos or "¡" in value_pos:
                value_pos_extra = re.sub('[^a-zA-Z0-9 \n\.]', '', value_pos)
                if value_pos_extra in positive_dict:
                    positive_sentiments += positive_dict[value_pos_extra] * 2
            value_pos = re.sub('[^a-zA-Z0-9 \n\.]', '', value_pos)
            if value_pos.isupper():
                value_pos = value_pos.lower()
                if value_pos in positive_dict:
                    positive_sentiments += positive_dict[value_tmp_pos] * 2

    for value_neg in tmp:
        value_tmp_neg = re.sub('[^a-zA-Z0-9 \n\.]', '', value_neg)
        value_tmp_neg = value_tmp_neg.lower()

        if value_tmp_neg in negative_dict:
            negative_sentiments += negative_dict[value_tmp_neg]
        if "!" in value_neg or "¡" in value_neg:
            value_neg_extra = re.sub('[^a-zA-Z0-9 \n\.]', '', value_neg)
            if value_neg_extra in negative_dict:
                negative_sentiments += negative_dict[value_tmp_neg] * 2
        value_neg = re.sub('[^a-zA-Z0-9 \n\.]', '', value_neg)
        if value_neg.isupper():
            value_neg = value_neg.lower()
            if value_neg in negative_dict:
                negative_sentiments += negative_dict[value_tmp_neg] * 2


    #print("positive: ", positive_sentiments, "negative: ", negative_sentiments)

    if positive_sentiments > negative_sentiments:
        return "positive"
    elif positive_sentiments < negative_sentiments:
        return "negative"
    else:
        return "neutral"



def main():
    data_cleaned = open_data()
    #data_complete, changeWord_complete = clean_data(data_cleaned)
    #to_import_RAE = import_data_to_RAE(data_complete, changeWord_complete)

    tweets_cleaned = open("fixedTweets.txt")
    tweets_cleaned_list = tweets_cleaned.readlines()

    data_cleaned.pop(0)

    for tweet in range(len(tweets_cleaned_list)):
        tmp = tweets_cleaned_list[tweet]
        sentiment = sentimental_analisys(tmp)
        #print(data_cleaned[tweet])
        print data_cleaned[tweet].decode("ISO-8859-1").encode('utf-8') + "|" + tmp.strip() + " | " + sentiment

if __name__ == '__main__':
    main()