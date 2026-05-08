import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def analyze_feedback(path):
    df = pd.read_csv(path)

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['feedback'])

    model = KMeans(n_clusters=2, random_state=42)
    df['cluster'] = model.fit_predict(X)

    return df