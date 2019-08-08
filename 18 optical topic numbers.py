import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import LatentDirichletAllocation

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(" ".join(line['NLP_text'].split(",")))
        print(NLP_word)
    comments_file.close()

    vectorizer = CountVectorizer(min_df=5, max_df=0.85)
    data_vectorized = vectorizer.fit_transform(NLP_word)

    search_params = {'n_components': [10, 15, 20, 25, 30], 'learning_decay': [.5, .7, .9]}
    lda = LatentDirichletAllocation(n_components=10, learning_method="batch",
                                    max_iter=25, random_state=0)
    model = GridSearchCV(lda, param_grid=search_params)
    model.fit(data_vectorized)
    GridSearchCV(cv=None, error_score='raise',
                 estimator=LatentDirichletAllocation(batch_size=128, doc_topic_prior=None,
                                                     evaluate_every=-1, learning_decay=0.7, learning_method=None,
                                                     learning_offset=10.0, max_doc_update_iter=100, max_iter=10,
                                                     mean_change_tol=0.001, n_components=10, n_jobs=1,
                                                     perp_tol=0.1, random_state=None,
                                                     topic_word_prior=None, total_samples=1000000.0, verbose=0),
                 iid=True, n_jobs=1,
                 param_grid={'n_topics': [10, 15, 20, 25, 30], 'learning_decay': [0.5, 0.7, 0.9]},
                 pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',
                 scoring=None, verbose=0)

    best_lda_model = model.best_estimator_
    print("Best Model's Params: ", model.best_params_)
    print("Best Log Likelihood Score: ", model.best_score_)
    print("Model Perplexity: ", best_lda_model.perplexity(data_vectorized))
