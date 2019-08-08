import csv
import gensim
from gensim import corpora
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import matplotlib.colors as mcolors

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='utf-8') as comments_file:
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
    print(lda_model.print_topics(num_topics=10, num_words=20))

    cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]

    cloud = WordCloud(background_color='white',
                      width=2500,
                      height=1800,
                      max_words=20,
                      colormap='tab10',
                      color_func=lambda *args, **kwargs: cols[i],
                      prefer_horizontal=1.0)

    topics = lda_model.show_topics(formatted=False)

    fig, axes = plt.subplots(2, 5, figsize=(20, 10))

    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
        plt.gca().axis('off')

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.tight_layout()
    plt.show()
