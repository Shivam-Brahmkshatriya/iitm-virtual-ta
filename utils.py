# utils.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_best_match(query, data):
    titles = [item["title"] for item in data]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(titles + [query])
    cosine_sim = cosine_similarity(tfidf[-1], tfidf[:-1])
    best_idx = cosine_sim.argmax()
    return data[best_idx]
