class Word:
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self._text
    
    def __add__(self, other):
        return Word(self._text + " " + other._text)
    
    def __sub__(self, other):
        return Word(self._text.replace(other._text, ""))

w1 = Word("Hello there")
w2 = Word("there")

w = w1 + w2
print(w)  # Output: Hello there
print(w1 - w2)