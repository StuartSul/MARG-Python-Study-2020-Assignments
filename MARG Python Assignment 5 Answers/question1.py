filename = input()
with open(filename, 'r') as textfile:
    text = textfile.read()

text = text.strip()
text = text.lower()
text = text.replace(',', '')
text = text.replace(';', '')
text = text.replace(':', '')
text = ' '.join(text.split())

sentences = text.split('.')[:-1]
squashed_sentences = [x.replace(' ', '') for x in sentences]
sentences_length = [len(x) for x in squashed_sentences]
character_count = sum(sentences_length)
avg_sentence_length = sum(sentences_length) / len(sentences_length)

text = text.replace('.', '')

words = text.split()
word_count = len(words)
word_frequency = {}
for word in words:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

print('Character Count: {}'.format(character_count))
print('Word Count: {}'.format(word_count))
print('Average Sentence Length: {} characters'.format(avg_sentence_length))
print('Word Frequency: ')
for word in sorted(word_frequency.keys()):
    print('  {}: {}'.format(word, word_frequency[word]))