import csv
from wordcloud import WordCloud
from matplotlib import pyplot as plt

if __name__ == '__main__':
    with open('YouTube_comments_NLP.csv', 'r', encoding='latin-1') as comments_file:
        comment_reader = csv.DictReader(comments_file, delimiter=',')
        NLP_word = []
        for line in comment_reader:
            NLP_word.append(line['NLP_text'])
        # print(NLP_word)
    comments_file.close()

    count_lst = []
    for item in NLP_word:
        count_lst.extend(item.split(","))
    # print(count_lst)

    cloud = WordCloud(background_color='white',
                      max_words=100,
                      max_font_size=40,
                      scale=3,
                      random_state=1  # chosen at random by flipping a coin; it was heads
                      ).generate(" ".join(count_lst))
    plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    plt.imshow(cloud, interpolation='bilinear')
    plt.show()

    cloud.to_file("word cloud.png")
