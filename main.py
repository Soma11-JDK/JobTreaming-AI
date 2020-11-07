import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


print(cosine_sim('a little bird', 'a little bird'))
print(cosine_sim('a flappy bird', 'bird'))
print(cosine_sim('a little bird', 'a big dog barks'))
print(cosine_sim('무료 파이썬 강의 추천', '파이썬'))
print(cosine_sim('프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)', '파이썬 입문'))