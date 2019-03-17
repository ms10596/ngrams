from Text import Text

def load(word):
        f = open('corpus.txt', encoding='utf-8')
        text = Text(f.read())
    #while True:
        #word = input()
        x = text.predict(word)
    #[print(i) for i in x]
        return x







