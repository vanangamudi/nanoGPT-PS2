import os
import re

pars=[]

with open('input.txt', 'r') as a:
    word = re.sub(r'\n\n\n+', '\n\n', a.read())
    print(word)
