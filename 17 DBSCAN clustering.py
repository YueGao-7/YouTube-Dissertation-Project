import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt


if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(" ".join(line['NLP_text'].split(",")))
        print(NLP_word)
    comments_file.close()

    vectorizer = TfidfVectorizer(min_df=5, max_df=0.85)
    tf_idf = vectorizer.fit_transform(NLP_word)
    feature_names = vectorizer.get_feature_names()
    num_samples, num_features = tf_idf.shape
    print("num_samples:  %d, num_features: %d" % (num_samples, num_features))
    dense = tf_idf.toarray()

    dbscan = DBSCAN()
    db = DBSCAN(eps=0.9, min_samples=3).fit(dense)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # Number of clusters in labels

    clusters1 = {}
    for c, i in enumerate(labels):
        if i == -1:
            continue
        elif i in clusters1:
            clusters1[i].append(NLP_word[c])
        else:
            clusters1[i] = [NLP_word[c]]
    for c in clusters1:
        print(clusters1[c])
        print()

    unique_labels = set(labels)
    colors = plt.get_cmap('Spectral')(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        class_member_mask = (labels == k)
        xy = dense[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markeredgecolor='k', markersize=14)
        xy = dense[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markeredgecolor='k', markersize=6)

    plt.axis([-0.5, 1.5, -0.5, 1.5])
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()


