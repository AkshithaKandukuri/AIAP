import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

df = pd.read_csv('social_media.csv')

def clean_text(text):
    text = str(text).lower()  # Convert to string and lowercase
    text = re.sub(r'<[^>]*>', '', text)  # Remove HTML tags
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = re.sub(r'\\d+', '', text)  # Remove numerical digits
    
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

df['cleaned_post_text'] = df['post_text'].apply(clean_text)

median_likes = df['likes'].median()
median_shares = df['shares'].median()

df['likes'] = df['likes'].fillna(median_likes)
df['shares'] = df['shares'].fillna(median_shares)

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()

df.drop_duplicates(inplace=True)

print("Cleaned Data Head:")
display(df.head())

print("\nCleaned Data Info:")
df.info()