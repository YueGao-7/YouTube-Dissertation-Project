import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

if __name__ == '__main__':
    stats = pd.read_csv('YouTube_videoStats_all.csv')

    stats.plot(kind='scatter', x='likeCount', y='commentCount', alpha=0.5, color='blue')
    x = stats['likeCount']
    y = stats['commentCount']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--")
    plt.xlabel('Like Counts')
    plt.ylabel('Comment Counts')
    plt.title('Like and Comment Counts Scatter Plot')
    plt.show()

    stats.plot(kind='scatter', x='dislikeCount', y='commentCount', alpha=0.5, color='red')
    x = stats['dislikeCount']
    y = stats['commentCount']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--")
    plt.xlabel('Dislike Counts')
    plt.ylabel('Comment Counts')
    plt.title('Dislike and Comment Counts Scatter Plot')
    plt.show()
