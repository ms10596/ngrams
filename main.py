from Text import Text
f = open('corpus.txt')
text = Text(f.read())


while True:
    word = input()
    x = text.predict(word)
    [print(i) for i in x]

