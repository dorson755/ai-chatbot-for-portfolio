from convokit import Corpus, download

# Download and load the Cornell Movie-Dialogs Corpus
corpus = Corpus(filename=download("movie-corpus"))

# Print summary statistics about the corpus
corpus.print_summary_stats()
