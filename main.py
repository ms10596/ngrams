from Text import Text
f = open('corpus.txt')
text = Text(f.read())


while True:

    word = input()
    x, y = text.predict(word)
    [print(i, j) for i,j in zip(x, y)]
    # [print(i) for i in y]

