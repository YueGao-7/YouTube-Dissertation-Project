import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import mglearn

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(" ".join(line['NLP_text'].split(",")))
        print(NLP_word)
    comments_file.close()

    vect = CountVectorizer(max_df=0.85)
    X = vect.fit_transform(NLP_word)
    lda = LatentDirichletAllocation(n_components=10, learning_method="batch",
                                    max_iter=25, random_state=0)
    document_topics = lda.fit_transform(X)

    sorting = np.argsort(lda.components_, axis=1)[:, ::-1]
    feature_names = np.array(vect.get_feature_names())
    mglearn.tools.print_topics(topics=range(10), feature_names=feature_names,
                               sorting=sorting, topics_per_chunk=10, n_words=20)
