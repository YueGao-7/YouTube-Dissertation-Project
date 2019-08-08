from __future__ import print_function
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


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

    sse = []
    for i in range(1, 30):
        km = KMeans(n_clusters=i, init='k-means++')
        km.fit(dense)
        sse.append(km.inertia_)
    plt.plot(range(1, 30), sse)
    plt.xticks(range(1, 30, 1))
    plt.title("The Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Sum of Squared Error")
    plt.show()
