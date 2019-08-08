import csv
import gensim
from gensim import corpora
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(line['NLP_text'].split(","))
        # print(NLP_word)
    comments_file.close()

    dictionary = corpora.Dictionary(NLP_word)
    doc_term_matrix = []
    for doc in NLP_word:
        doc_term_matrix.append(dictionary.doc2bow(doc))

    lda = gensim.models.ldamodel.LdaModel
    lda_model = lda(doc_term_matrix, num_topics=10, id2word=dictionary, passes=10)
    # print(lda_model.print_topics(num_topics=10, num_words=20))

    topics = lda_model.show_topics(formatted=False)
    data_flat = [w for w_list in NLP_word for w in w_list]
    counter = Counter(data_flat)

    out = []
    for i, topic in topics:
        for word, weight in topic:
            out.append([word, i, weight, counter[word]])

    df = pd.DataFrame(out, columns=['word', 'topic_id', 'importance', 'word_count'])

    fig, axes = plt.subplots(2, 5, figsize=(80, 20), dpi=55)
    cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]
    for i, ax in enumerate(axes.flatten()):
        ax.bar(x='word', height="word_count", data=df.loc[df.topic_id == i, :], color=cols[i], width=0.5, alpha=0.3,
               label='Word Count')
        ax_twin = ax.twinx()
        ax_twin.bar(x='word', height="importance", data=df.loc[df.topic_id == i, :], color=cols[i], width=0.2,
                    label='Weights')
        ax.set_ylabel('Word Count', color=cols[i])
        ax_twin.set_ylim(0, 0.15)
        ax.set_ylim(0, 2500)
        ax.set_title('Topic: ' + str(i), color=cols[i], fontsize=12)
        ax.tick_params(axis='y', left=False)
        ax.set_xticklabels(df.loc[df.topic_id == i, 'word'], rotation=30, horizontalalignment='right')
        ax.legend(loc='upper left')
        ax_twin.legend(loc='upper right')

    fig.tight_layout()
    fig.subplots_adjust(top=0.90, bottom=0.1, wspace=0.3, hspace=0.3)
    fig.suptitle('Word Count and Weights of Topic Keywords', fontsize=10, y=1.05)
    plt.show()
