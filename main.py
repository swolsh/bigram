import torch
import string
import numpy

with open('names.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', '').replace('\r', '').lower()

data = ''.join(filter(str.isalpha, data))

bigrams = []
for i in range(len(data) - 1):
    bigrams.append(data[i:i + 2])

bigram_counts = {}
for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1

total_bigrams = sum(bigram_counts.values())

bigram_probabilities = {}
for bigram in bigram_counts:
    bigram_probabilities[bigram] = bigram_counts[bigram] / total_bigrams

import numpy as np


def generate_name(bigram_probabilities):
    letters = sorted(list(set(''.join(list(bigram_probabilities.keys())))))

    letter_probabilities = np.array([sum(bigram_probabilities.get(f'{letter1}{letter2}', 0)
                                         for letter2 in letters) for letter1 in letters])
    letter_probabilities /= sum(letter_probabilities)

    first_letter_index = np.random.choice(len(letters), p=letter_probabilities)
    name = letters[first_letter_index]
    return name

for i in range(10):
    print(generate_name(bigram_probabilities))
