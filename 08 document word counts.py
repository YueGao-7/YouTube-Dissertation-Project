import csv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(line['NLP_text'].split(","))
        print(NLP_word)
    comments_file.close()

    doc_lens = []
    for item in NLP_word:
        doc_lens.append(len(item))

    plt.figure()
    plt.hist(doc_lens, bins=500, color='navy')
    plt.text(75, 1000, "Mean   : " + str(round(np.mean(doc_lens))))
    plt.text(75, 900, "Median : " + str(round(np.median(doc_lens))))
    plt.text(75, 800, "Stdev   : " + str(round(np.std(doc_lens))))
    plt.text(75, 700, "1%ile    : " + str(round(np.quantile(doc_lens, q=0.01))))
    plt.text(75, 600, "99%ile  : " + str(round(np.quantile(doc_lens, q=0.99))))

    plt.gca().set(xlim=(0, 120), ylabel='Number of Documents', xlabel='Document Word Count')
    plt.tick_params(size=16)
    plt.xticks(np.linspace(0, 120, 6))
    plt.title('Distribution of Document Word Counts', fontdict=dict(size=22))
    plt.show()
