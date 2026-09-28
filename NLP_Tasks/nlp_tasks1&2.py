import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------
# 1. Create a corpus of 7 sentences
# ---------------------------------------

corpus = [
    "I love machine learning",
    "Machine learning is interesting",
    "I love programming",
    "Programming is very interesting",
    "I love artificial intelligence",
    "Artificial intelligence uses machine learning",
    "Machine learning and programming are useful"
]

# ---------------------------------------
# 2. Create Bag of Words
# ---------------------------------------

vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(corpus)

# Convert BoW matrix to NumPy array
bow_array = bow_matrix.toarray()

# Get vocabulary
words = vectorizer.get_feature_names_out()

# ---------------------------------------
# 3. Display Vocabulary
# ---------------------------------------

print("Vocabulary:")
print(words)

# ---------------------------------------
# 4. Display Bag of Words using Pandas
# ---------------------------------------

df_bow = pd.DataFrame(
    bow_array,
    columns=words,
    index=[f"Sentence {i+1}" for i in range(len(corpus))]
)

print("\nBag of Words:")
print(df_bow)

# ---------------------------------------
# 5. Calculate Cosine Similarity
# ---------------------------------------

similarity_matrix = cosine_similarity(bow_matrix)

# Convert similarity matrix into Pandas DataFrame
df_similarity = pd.DataFrame(
    similarity_matrix,
    columns=[f"Sentence {i+1}" for i in range(len(corpus))],
    index=[f"Sentence {i+1}" for i in range(len(corpus))]
)

# ---------------------------------------
# 6. Display Cosine Similarity
# ---------------------------------------

print("\nCosine Similarity:")
print(df_similarity.round(2))

# ---------------------------------------
# 7. Find similarity between two sentences
# ---------------------------------------

sentence1 = 0
sentence2 = 1

similarity = cosine_similarity(
    bow_matrix[sentence1],
    bow_matrix[sentence2]
)

print(
    f"\nSimilarity between Sentence 1 and Sentence 2: "
    f"{similarity[0][0]:.4f}"
)