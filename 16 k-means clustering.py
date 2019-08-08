from __future__ import print_function
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(" ".join(line['NLP_text'].split(",")))
        # print(NLP_word)
    comments_file.close()

    vectorizer = TfidfVectorizer(min_df=5, max_df=0.85)
    tf_idf = vectorizer.fit_transform(NLP_word)
    feature_names = vectorizer.get_feature_names()
    num_samples, num_features = tf_idf.shape
    print("num_samples:  %d, num_features: %d" % (num_samples, num_features))
    dense = tf_idf.toarray()

    n_clusters = 10
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100)
    kmeans.fit(dense)
    centres = kmeans.cluster_centers_
    print(Counter(kmeans.labels_))

    print("Top terms per cluster:")
    order_centroids = centres.argsort()[:, ::-1]
    for i in range(n_clusters):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :n_clusters]:
            print(' %s' % feature_names[ind]),
        print()

    pca = PCA(n_components=2)
    coords = pca.fit_transform(dense)
    centres_coords = pca.fit_transform(centres)
    cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]
    plt.figure()
    for j in range(n_clusters):
        plt.scatter(coords[:, 0], coords[:, 1], c=cols[j], marker="x")
        plt.scatter(centres_coords[:, 0], centres_coords[:, 1], c="k")
    plt.show()


