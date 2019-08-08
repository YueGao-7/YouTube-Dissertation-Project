import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

if __name__ == '__main__':
    stats = pd.read_csv('YouTube_videoStats_all.csv',
                        usecols=["viewCount", "likeCount", "dislikeCount", "commentCount"])

    print(stats.corr())  # create correlation matrix
    print(stats.corr()['viewCount'].sort_values(ascending=False))  # like is the most strongly correlated to view

    scatter_matrix(stats, figsize=(20, 12), alpha=0.3)
    plt.show()
