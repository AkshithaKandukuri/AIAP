import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
df = pd.read_csv('/content/movie_reviews-1.csv')

# Standardize text (lowercase and remove HTML tags)
df['review_text'] = df['review_text'].str.lower()
df['review_text'] = df['review_text'].apply(lambda x: re.sub(r'<[^>]+>', '', x))

# Handle missing ratings (fill with median)
median_rating = df['rating'].median()
df['rating'] = df['rating'].fillna(median_rating)

# Normalize ratings (0-10 to 0-1 scale)
df['rating'] = df['rating'] / 10

# Tokenize and encode reviews using TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['review_text'])

print("Final Processed Data Head:")
display(df.head())

print("\nShape of the TF-IDF matrix:")
print(tfidf_matrix.shape)