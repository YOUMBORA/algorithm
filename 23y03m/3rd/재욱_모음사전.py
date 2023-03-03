from itertools import product as pd

def solution(word):
    dic = "AEIOU"
    vocab = []
    for i in range(5):
        for t in pd(dic, repeat=i+1):
            words = ''.join(t)
            vocab.append(words)
            
            if word == words:
                break

    vocab.sort()

    return vocab.index(word) + 1

