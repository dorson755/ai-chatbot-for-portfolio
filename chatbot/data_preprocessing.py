from convokit import Corpus, download
import re
import random
from sklearn.model_selection import train_test_split

# Download and load the Cornell Movie Dialogs Corpus
corpus = Corpus(download('movie-corpus'))

# Print summary statistics
print(corpus.print_summary_stats())

# Function to clean the text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove punctuation
    text = text.lower()  # Normalize to lowercase
    return text.strip()

# Create input-output pairs from the conversations
def create_input_output_pairs(corpus, num_pairs=1000):
    pairs = []
    for i in range(num_pairs):
        convo = corpus.random_conversation()
        for _utterance_id in convo._utterance_ids:
            utterance = corpus.get_utterance(_utterance_id)
            cleaned_text = clean_text(utterance.text)
            if len(cleaned_text.split()) > 1:  # Avoid single-word utterances
                if _utterance_id != convo._utterance_ids[0]:  # Skip the first utterance
                    prev_utterance = corpus.get_utterance(convo._utterance_ids[convo._utterance_ids.index(_utterance_id) - 1])
                    pairs.append((clean_text(prev_utterance.text), cleaned_text))
    return pairs

# Create input-output pairs
pairs = create_input_output_pairs(corpus)
print(f"Number of input-output pairs created: {len(pairs)}")

# Split the data into training and testing sets
train_pairs, test_pairs = train_test_split(pairs, test_size=0.2, random_state=42)

print(f"Training pairs: {len(train_pairs)}, Testing pairs: {len(test_pairs)}")

# Example of input-output pairs
for i in range(3):  # Print a few examples
    print(f"Input: {train_pairs[i][0]}, Output: {train_pairs[i][1]}")
