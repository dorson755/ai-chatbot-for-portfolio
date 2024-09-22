from convokit import Corpus, download

# Download and load the Cornell Movie Dialogs Corpus
corpus = Corpus(download('movie-corpus'))

# Print summary statistics
print(corpus.print_summary_stats())

# Extracting a few random conversations
for i in range(3):  # Change the range for more conversations
    convo = corpus.random_conversation()
    print(f"Conversation ID: {convo.id}")
    
    # Access the utterances using the correct attribute
    for _utterance_id in convo._utterance_ids:
        utterance = corpus.get_utterance(_utterance_id)
        print(f"Speaker: {utterance.speaker.id}, Text: {utterance.text}")
    print("\n" + "="*40 + "\n")
