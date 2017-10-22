import json

from pprint import pprint



with open('face.data') as data_file:
    data = json.load(data_file)

pprint(data)