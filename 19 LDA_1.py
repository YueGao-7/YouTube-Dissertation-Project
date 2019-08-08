import csv
import gensim
from gensim import corpora

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(line['NLP_text'].split(","))
        print(NLP_word)
    comments_file.close()

    dictionary = corpora.Dictionary(NLP_word)
    doc_term_matrix = []
    for doc in NLP_word:
        doc_term_matrix.append(dictionary.doc2bow(doc))

    lda = gensim.models.ldamodel.LdaModel
    lda_model = lda(doc_term_matrix, num_topics=10, id2word=dictionary, passes=10)
    for i, topic in lda_model.show_topics(formatted=True, num_topics=10, num_words=20):
        print(str(i) + ": " + topic)
        print()

    print(lda_model[doc_term_matrix[1]])





