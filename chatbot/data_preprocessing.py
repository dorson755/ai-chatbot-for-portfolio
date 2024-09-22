import pandas as pd

# Load movie lines
lines_file = './data/cornell_movie_dialogs_corpus/movie_lines.txt'
conversations_file = './data/cornell_movie_dialogs_corpus/movie_conversations.txt'

# Read lines
lines = pd.read_csv(lines_file, sep='+++$+++', header=None, names=['line_id', 'character', 'movie', 'text'], engine='python')
lines['line_id'] = lines['line_id'].str.strip()

# Read conversations
conversations = pd.read_csv(conversations_file, sep='+++$+++', header=None, names=['character1', 'character2', 'lines'], engine='python')

# Display the first few rows
print(lines.head())
print(conversations.head())
