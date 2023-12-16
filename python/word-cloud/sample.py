import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_word_cloud(filename):
    with open(filename, 'r') as file:
        text = file.read()

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

create_word_cloud('info.txt')