from collections import Counter

from nltk import word_tokenize, ngrams


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
        for bigram in self.bigrams:
            word_with_other_two_words = ((word,) + bigram)
            # print(word_with_other_two_words)
            possibilities.append(word_with_other_two_words)
            probabilities.append(
                self.probability(self.tri_probability(word_with_other_two_words), self.bi_probability(bigram)))
            # print(probabilities[-1])
        possibilities, probabilities = zip(*sorted(zip(possibilities, probabilities), key=lambda t: t[1], reverse=True))
        return set(possibilities[:10]), probabilities[:10]

    def tri_probability(self, trigram):
        if self.tricounter.get(trigram) is not None:
            return self.tricounter.get(trigram) / len(trigram)
        return 0

    def bi_probability(self, bigram):
        if self.bicounter.get(bigram) is not None:
            return self.bicounter.get(bigram) / len(bigram)
        return 0
    def probability(self, a, b):
        return a / b if b > 0 else 0
