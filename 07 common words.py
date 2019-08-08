import csv
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(line['NLP_text'])
        print(NLP_word)
    comments_file.close()

    count_lst = []
    for item in NLP_word:
        count_lst.extend(item.split(","))
    print(count_lst)

    first_counts = Counter(count_lst).most_common(20)
    print(first_counts)
    labels = list(zip(*first_counts))[0]
    values = list(zip(*first_counts))[1]
    x_pos = np.arange(len(labels))

    plt.bar(x_pos, values, align='center')
    plt.xticks(x_pos, labels)
    plt.ylabel('Number of Words')
    plt.title("Top 20 most common words")
    plt.show()
