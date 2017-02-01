import yaml
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_yaml(path):
    with open(path, 'r') as stream:
        try:
            return(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)


def load_words():
    wordsDict = load_yaml(os.path.join(BASE_DIR, 'data/words.yaml'))
    return wordsDict['words']
