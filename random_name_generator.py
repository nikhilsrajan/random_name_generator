import sys
import random


def generate_random_name():
    with open('nouns.txt', 'r') as h: nouns = [word.replace('\n', '') for word in h.readlines()]
    with open('adjectives.txt', 'r') as h: adjectives = [word.replace('\n', '') for word in h.readlines()]
    with open('verbs.txt', 'r') as h: verbs = [word.replace('\n', '') for word in h.readlines()]
    return f'{random.choice(verbs)}_{random.choice(adjectives)}_{random.choice(nouns)}'


if __name__ == '__main__':
    N = 1
    if len(sys.argv) > 1:
        arg:str = sys.argv[1]
        if arg.isnumeric():
            N = int(arg)
            
    for _ in range(N):
        print(generate_random_name())
