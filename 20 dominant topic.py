import csv
import gensim
from gensim import corpora
import pandas as pd

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
    print(lda_model.print_topics(num_topics=10, num_words=20))


    def format_topics_sentences(ldamodel=None, corpus=doc_term_matrix, texts=NLP_word):
        sent_topics_df = pd.DataFrame()

        for i, row_list in enumerate(ldamodel[corpus]):
            row = row_list[0] if ldamodel.per_word_topics else row_list
            # print(row)
            row = sorted(row, key=lambda x: (x[1]), reverse=True)
            for j, (topic_num, prop_topic) in enumerate(row):
                if j == 0:
                    wp = ldamodel.show_topic(topic_num)
                    topic_keywords = ", ".join([word for word, prop in wp])
                    sent_topics_df = sent_topics_df.append(
                        pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]), ignore_index=True)
                else:
                    break
        sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

        contents = pd.Series(texts)
        sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
        return sent_topics_df


    df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model, corpus=doc_term_matrix, texts=NLP_word)

    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
    pd.set_option('display.max_columns', None)
    print(df_dominant_topic.head(10))
