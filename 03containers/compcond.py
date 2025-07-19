words1 = ["it", "was", "the", "best", "of", "times"]

words2 = [w for w in words1]
print(words2)

words3 = [w for w in words1 if len(w) > 3]
print(words3)

words4 = [w.upper() if len(w) > 3 else w for w in words1 if len(w) > 3]
print(words4)

words5 = [w.upper() if len(w) > 3 else w for w in words1]
print(words5)

