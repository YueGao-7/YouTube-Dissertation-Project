import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from matplotlib import pyplot as plt


if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(" ".join(line['NLP_text'].split(",")))
        print(NLP_word)
    comments_file.close()

    cv = CountVectorizer(min_df=5, max_df=0.85)
    doc_term_matrix = cv.fit_transform(NLP_word)
    # print(doc_term_matrix.shape)
    # print(list(cv.vocabulary_.keys())[:10])
    feature_names = cv.get_feature_names()
    count = doc_term_matrix.toarray().sum(axis=0)

    vectorizer = TfidfVectorizer(min_df=5, max_df=0.85)
    X = vectorizer.fit_transform(NLP_word)
    num_samples, num_features = X.shape
    tf = count / num_samples
    idf = vectorizer.idf_

    transformer = TfidfTransformer()
    transformed_weights = transformer.fit_transform(doc_term_matrix)
    tf_idf = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
    weights_df = pd.DataFrame({'term': feature_names, 'count': count, 'tf': tf, 'idf': idf, 'tf-idf': tf_idf})

    head_20 = weights_df.sort_values(by='tf-idf', ascending=False).head(20)
    print(head_20)
    plt.figure(figsize=(3, 15))
    plt.bar(head_20['term'], head_20['tf-idf'], align='center', width=0.5, color='grey')
    plt.xlabel('term', fontsize=14)
    plt.ylabel("Mean Tf-Idf Score")
    plt.title("Top 20 Tf-Idf Scores")
    plt.show()


