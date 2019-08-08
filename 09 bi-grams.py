import csv
from nltk import bigrams
import itertools
from collections import Counter
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(line['NLP_text'].split(","))
        # print(NLP_word)
    comments_file.close()

    bi_terms = []
    for item in NLP_word:
        bi_terms.append(list(bigrams(item)))

    bigm = list(itertools.chain(*bi_terms))
    bigm_counts = Counter(bigm).most_common(50)
    bigm_df = pd.DataFrame(bigm_counts, columns=['bigram', 'count'])
    print(bigm_df)  # get df: paired keywords & counts

    d = bigm_df.set_index('bigram').T.to_dict('records')
    G = nx.Graph()
    for k, v in d[0].items():
        G.add_edge(k[0], k[1], weight=(v * 10))

    fig, ax = plt.subplots(figsize=(14, 12))
    pos = nx.spring_layout(G, k=1)

    nx.draw_networkx(G, pos,
                     font_size=9,
                     width=2,
                     edge_color='grey',
                     node_color='purple',
                     node_size=10,
                     with_labels=False,
                     ax=ax)

    for key, value in pos.items():
        x, y = value[0] + .01, value[1] + .01
        ax.text(x, y,
                s=key,
                horizontalalignment='center', fontsize=8)

    plt.title("plot of top 50 co-occurring bigram words ")
    plt.show()
