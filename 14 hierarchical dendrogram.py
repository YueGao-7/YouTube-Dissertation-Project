import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

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

    plt.figure()
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('words')
    plt.ylabel('Distances')
    dendrogram(
        linkage(dense, 'ward'),
        leaf_rotation=90,
        leaf_font_size=8,
    )
    plt.show()

