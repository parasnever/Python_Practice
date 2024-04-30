import json

import numpy as np

a = np.zeros(10)
print(a)
b = np.full((2,10),0.7)
print(b)
c = np.linspace(0,25,7)
print(c)
print(type(c))


#pandas packages

import pandas as pd

a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                  'Sounds':['Barks',"Meow",'Roars','Moo',"Trumpet"]})
print(a)

print(a.describe())

b = pd.DataFrame({
    "Letters":['a','b','c','d','e','f'],
    'Numbers':[12,7,9,3,5,1]
})
print(b.sort_values(by ="Numbers"))
b = b.assign(new_values = b['Numbers'] *3)
print(b)

#NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# Print statement 1
print(word_tokenize(text))
# Print statement 2
print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)

