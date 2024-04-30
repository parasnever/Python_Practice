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
from nltk.tol
