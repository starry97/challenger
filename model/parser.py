import json

from pprint import pprint

with open('face.data', encoding = 'utf-8') as data_file:
    data = json.load(data_file)

pprint(data)