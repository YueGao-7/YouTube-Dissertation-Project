import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

if __name__ == '__main__':
    NLP = pd.read_csv('YouTube_comments_NLP.csv')

    stats = pd.read_csv('YouTube_videoStats_all.csv')
    max_view = stats[stats.commentCount != 0].nlargest(10, 'viewCount')
    join_df = pd.merge(max_view, NLP, on='videoId', how='left')
    join_df_ = join_df[np.isfinite(join_df['commentCount'])]

    result = []
    title = []
    for row in max_view['videoId']:
        line = []
        for word in join_df_[join_df_.videoId == row].NLP_text:
            line.append(word)
        # try:
        str_line = ",".join(map(str, line))
        # except TypeError as e:
        #     str_line = ""
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

    plt.bar(x_pos, values, align='center')
    plt.xticks(x_pos, labels)
    plt.ylabel('Number of Words')
    plt.title("Max_View: Top 20 most common words")
    plt.show()
