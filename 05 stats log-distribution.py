import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

if __name__ == '__main__':
    stats = pd.read_csv('YouTube_videoStats_all.csv')
    # print(stats.shape)
    # print(stats.info())

    stats['views_log'] = np.log(stats['viewCount'] + 1)
    stats['likes_log'] = np.log(stats['likeCount'] + 1)
    stats['dislikes_log'] = np.log(stats['dislikeCount'] + 1)
    stats['comment_count_log'] = np.log(stats['commentCount'] + 1)

    plt.figure(figsize=(12, 6))
    plt.subplot(221)
    g1 = sns.distplot(stats['likes_log'], color='green')
    g1.set_title("LIKES LOG DISTRIBUTION", fontsize=16)

    plt.subplot(222)
    g2 = sns.distplot(stats['views_log'])
    g2.set_title("VIEWS LOG DISTRIBUTION", fontsize=16)

    plt.subplot(223)
    g3 = sns.distplot(stats['dislikes_log'], color='r')
    g3.set_title("DISLIKES LOG DISTRIBUTION", fontsize=16)

    plt.subplot(224)
    g4 = sns.distplot(stats['comment_count_log'])
    g4.set_title("COMMENT COUNT LOG DISTRIBUTION", fontsize=16)

    plt.subplots_adjust(wspace=0.2, hspace=0.4, top=0.9)

    plt.show()
