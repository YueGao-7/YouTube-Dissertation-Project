import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

if __name__ == '__main__':
    NLP = pd.read_csv('YouTube_comments_NLP.csv')
    # print(NLP)

    stats = pd.read_csv('YouTube_videoStats_all.csv')
    max_like = stats.nlargest(10, 'likeCount')
    join_df = pd.merge(max_like, NLP, on='videoId', how='left')
    join_df_ = join_df[np.isfinite(join_df['commentCount'])]

    result = []
    title = []
    for row in max_like['videoId']:
        line = []
        for word in join_df_[join_df_.videoId == row].NLP_text:
            line.append(word)
        str_line = ",".join(map(str, line))
        result.append(str_line)
        title.append(row)

    data = {'videoId': Series(title),
            'text': Series(result)}
    new_df = DataFrame(data)
    print(new_df)

    count_lst = []
    for item in new_df["text"]:
        count_lst.extend(item.split(","))
    # print(count_lst)

    first_counts = Counter(count_lst).most_common(20)
    # print(first_counts)
    labels = list(zip(*first_counts))[0]
    values = list(zip(*first_counts))[1]
    x_pos = np.arange(len(labels))

    plt.bar(x_pos, values, align='center', color='green')
    plt.xticks(x_pos, labels)
    plt.ylabel('Number of Words')
    plt.title("Max_Like: Top 20 most common words")
    plt.show()
