import csv
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import enchant

if __name__ == '__main__':
    with open('YouTube_comments_all.csv', 'r', encoding='utf-8') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        word_tokens = []
        stop_words = set(stopwords.words('english'))
        table = str.maketrans("", "", string.punctuation)
        auther_name = ["david", "greg", "martin", "langer", "raval", "siraj"]
        en = enchant.Dict("en_US")
        irrelevant_words = ["fuck", "fucker", "shit", "bullshit", "shittier", "shitty", "email", "hi", "hello", "u",
                            "x", "b"]
        wordnet_lemmatizer = WordNetLemmatizer()
        url_list = []
        for line in comment_reader:
            url = (re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line['text']))
            url_list.extend(url)
            temp = word_tokenize(line['text'].lower())
            videoId = line['videoId']
            newtemp = []
            for word in temp:
                if word.translate(table) != "":
                    if word.translate(table) not in stop_words:
                        if not word.translate(table).isdigit():
                            if word.translate(table) not in auther_name:
                                if en.check(word.translate(table)):
                                    if wordnet_lemmatizer.lemmatize(word.translate(table),
                                                                    pos='v') not in irrelevant_words:
                                        newtemp.append(wordnet_lemmatizer.lemmatize(word.translate(table), pos='v'))
                            else:
                                if wordnet_lemmatizer.lemmatize(word.translate(table),
                                                                pos='v') not in irrelevant_words:
                                    newtemp.append(wordnet_lemmatizer.lemmatize(word.translate(table), pos='v'))
            newtemp.extend(url)
            newlst = ','.join(newtemp)
            word_tokens.append([videoId, newlst])
    comments_file.close()

    print(word_tokens)
    print(url_list)

    with open("YouTube_comments_NLP.csv", "w",  newline='', encoding='utf-8') as NLP_file:
        comment_writer = csv.writer(NLP_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        comment_writer.writerows([["videoId", "NLP_text"]])
        for item in word_tokens:
            comment_writer.writerows([item])
