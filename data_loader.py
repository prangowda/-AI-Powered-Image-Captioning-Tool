import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Load dataset
df = pd.read_csv("captions.csv")

# Tokenize sentences
nltk.download("punkt")
df["tokens"] = df["caption"].apply(lambda x: word_tokenize(x.lower()))

# Save processed data
df.to_csv("processed_captions.csv", index=False)
print("Dataset processed successfully.")
