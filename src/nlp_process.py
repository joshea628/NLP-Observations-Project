from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from justin_clean_pipeline import pipeline
import numpy as np
from PIL import Image
from os import path

file = '../data/ufo_first100records.json'
other_stuff, documents = pipeline(file) #insert cleaned data here

def token_stop_stem_lem(documents):
    #tokenize words
    docs = [word_tokenize(content) for content in documents]

    #strip stopwords
    stop = stopwords.words('english')
    stop.append('nuforc')
    stop = set(stop)
    docs = [[word for word in words if word not in stop and word.isalnum()] for words in docs]

    #stem/lem options. here are all of them, once we use the data we can eliminate options
    porter = PorterStemmer()
    snowball = SnowballStemmer('english')
    wordnet = WordNetLemmatizer()
    docs_porter = [[porter.stem(word) for word in words] for words in docs]
    docs_snowball = [[snowball.stem(word) for word in words] for words in docs]
    docs_wordnet = [[wordnet.lemmatize(word) for word in words] for words in docs]

    return docs_porter, docs_snowball, docs_wordnet, docs

def bag_of_words(docs):
    '''
    Creates a bag of words for inputted array
    '''
    bag_set = set()
    [[bag_set.add(token) for token in tokens] for tokens in docs]
    vocab = list(bag_set)
    return vocab

def tf_idf(documents):
    '''
    Creates a TF-IDF matrix based on the original data
    '''
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorized = vectorizer.fit_transform(documents)
    features = vectorizer.get_feature_names()
    return vectorized, features

def cosine_sim(vectorized):
    '''
    Calculates pairwise similarity for tf-idf matrix
    '''
    cosine_sims = linear_kernel(vectorized, vectorized)
    return cosine_sims

def word_cloud(vectorized):
    '''
    Creates a wordcloud for the inputted array of words, assumes stopwords have already been 
    removed
    '''
    alien_mask = np.array(Image.open("../images/alien.jpg"))
    wordcloud = WordCloud(width=1000, height=1000, background_color='white', 
                            min_font_size=9, mask=alien_mask).generate(vectorized)
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud)
    plt.axis('off')
    #plt.show()
    plt.savefig('../images/wordcloud.png')

if __name__ == '__main__':
    file = '../data/ufo_first100records.json'
    other_stuff, documents = pipeline(file)
    #print(documents[0])
    docs_porter, docs_snowball, docs_wordnet, docs= token_stop_stem_lem(documents)
    vectorized, features = tf_idf(documents)
    flat_words = []
    for sublist in docs_wordnet:
        for item in sublist:
            flat_words.append(item)
    # for sublist in features:
    #     flat_words.append(sublist)
    string_of_words = ' '.join(flat_words)
    word_cloud(string_of_words)
    #print(features)