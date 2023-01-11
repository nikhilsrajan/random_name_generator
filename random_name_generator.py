import sys
import random
import os


def generate_random_name(sep='_'):
    random.seed()   # unsetting seed
    package_dir = os.path.dirname(__file__)
    nouns_filepath = os.path.join(package_dir, 'nouns.txt')
    adjectives_filepath = os.path.join(package_dir, 'adjectives.txt')
    verbs_filepath = os.path.join(package_dir, 'verbs.txt')
    with open(nouns_filepath, 'r') as h: nouns = [word.replace('\n', '') for word in h.readlines()]
    with open(adjectives_filepath, 'r') as h: adjectives = [word.replace('\n', '') for word in h.readlines()]
    with open(verbs_filepath, 'r') as h: verbs = [word.replace('\n', '') for word in h.readlines()]
    random_name = f'{random.choice(verbs)}{sep}{random.choice(adjectives)}{sep}{random.choice(nouns)}'
    return random_name


if __name__ == '__main__':
    N = 1
    if len(sys.argv) > 1:
        arg:str = sys.argv[1]
        if arg.isnumeric():
            N = int(arg)
            
    for _ in range(N):
        print(generate_random_name())
