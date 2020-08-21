from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from wordcloud import WordCloud
import matplotlib.pyplot as plt

documents = None #insert cleaned data here

def token_stop_stem_lem(documents):
    #tokenize words
    docs = [word_tokenize(content) for content in documents]

    #strip stopwords
    stopwords = set(stopwords.words('english'))
    docs = docs = [[word for word in words if word not in stopwords] for words in docs]

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
    return vectorized

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
    wordcloud = WordCloud(width=800, height=800, background_color='black', 
                            min_font_size=10).generate(vectorized)
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

