import pandas as pd

# Load movie lines and conversations
lines_file = './data/cornell_movie_dialogs_corpus/movie_lines.tsv'
conversations_file = './data/cornell_movie_dialogs_corpus/movie_conversations.tsv'

# Read lines (using the correct separator for TSV)
lines = pd.read_csv(lines_file, sep='\t', header=None, names=['line_id', 'character', 'movie', 'text'])

# Read conversations
conversations = pd.read_csv(conversations_file, sep='\t', header=None, names=['character1', 'character2', 'lines'])

# Display the first few rows
print(lines.head())
print(conversations.head())

# Create a list to hold questions and answers
questions = []
answers = []

# Extracting the conversations
for index, row in conversations.iterrows():
    line_ids = row['lines'].strip().split(' ')
    
    for i in range(len(line_ids) - 1):
        questions.append(lines.loc[lines['line_id'] == line_ids[i], 'text'].values[0])
        answers.append(lines.loc[lines['line_id'] == line_ids[i + 1], 'text'].values[0])

# Create a DataFrame for the questions and answers
qa_pairs = pd.DataFrame({'question': questions, 'answer': answers})

# Display the first few question-answer pairs
print(qa_pairs.head())
