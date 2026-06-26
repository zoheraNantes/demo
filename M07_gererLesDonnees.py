import json

import chardet
import pickle


with open('fichier_unicode.txt', 'rb') as f:
    encoding = chardet.detect(f.read())

with open('fichier_unicode.txt', 'r+', encoding=encoding['encoding']) as f:
    print(f.read())


l = ['a','b','c']

serialized = json.dumps(l)
print(type(serialized))

deserialized = json.loads(serialized)
print(type(deserialized))

serialized = pickle.dumps(l)
print(type(serialized))

deserialized = pickle.loads(serialized)
print(type(deserialized))

serialized = pickle.dump(l, open('serialized.p', 'wb'))
print(type(serialized))

deserialized = pickle.load(open('serialized.p', 'rb'))
print(type(deserialized))
