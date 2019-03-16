from collections import Counter

from nltk import word_tokenize, ngrams


def probability(a, b):
    return a / b if b > 0 else 0


class Text:
    def __init__(self, raw):
        self.raw = raw

        self.words = word_tokenize(self.raw)

        self.bigrams = list(ngrams(self.words, 2))
        self.bicounter = Counter(self.bigrams)

        self.trigrams = list(ngrams(self.words, 3))
        self.tricounter = Counter(self.trigrams)

    def predict(self, word):
        possibilities = []
        probabilities = []
        for bigram,frequency in self.bicounter.items():
            word_with_other_two_words = ((word,) + bigram)
            possibilities.append(word_with_other_two_words)
            probabilities.append(
                probability(self.tri_probability(word_with_other_two_words), self.bi_probability(bigram)))
        possibilities, probabilities = zip(*sorted(zip(possibilities, probabilities), key=lambda t: t[1], reverse=True))
        return [(possibilities[i],probabilities[i]) for i in range(len(probabilities[:10])) if probabilities[i] > 0]

    def tri_probability(self, trigram):
        if self.tricounter.get(trigram) is not None:
            return self.tricounter.get(trigram) / len(trigram)
        return 0

    def bi_probability(self, bigram):
        if self.bicounter.get(bigram) is not None:
            return self.bicounter.get(bigram) / len(bigram)
        return 0
