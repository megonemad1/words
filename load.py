import pprint
import csv

def load(path):
    with open(path,'r') as f:
        return [x for x in f.read().split('\n') if x != '']

if __name__=='__main__':
    pprint.pprint(load('Adjectives.csv'))
