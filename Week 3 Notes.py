import pandas as pd
import json

Bond = {'Father': 'James Bond', 'Mother': 'Maria Bond', 'Daughter': 'Consuela Bond', 'Son': 'Jack Bond'}
Hernandez = {'Father': 'Caesar Hernandez', 'Mother': 'Gloria Hernandez', 'Daughter': 'Lupe Hernandez',
             'Son': 'Carlito Hernandez'}
Nazari = {'Father': 'Ali Nazari', 'Mother': 'Samira Nazari', 'Daughter': '', 'Son': 'Abdi Nazari'}
Green = {'Father': 'Thomas Green', 'Mother': 'Claire Green', 'Daughter': 'Zoe Green', 'Son': ''}
Singh = {'Father': 'Amar Singh', 'Mother': 'Chuni Singh', 'Daughter': 'Greysi Singh', 'Son': 'Haashim Singh'}
families = [Bond, Hernandez, Nazari, Green, Singh]

file = open('new_families.txt', 'r')

print(file)
print(type(file))
