
'''
JSON stands for JavaScript OBJECT Notation
JSON looks very similar to a python dictionary with the following exceptions:
JSON keys must be strigs but python dictionary keys can have any immutable type
True in python becames true in JSON
False in python becomes False in JSON
None in python becomes null in JSON
JSON strings must have double quotes but dictionary strings can be double or single quote
'''
import json
# json.dumps takes a python dictionary and converts it to a JSON string
to_json = {"flag":True, "name":"donnie"}
print("dictionary", to_json)
now_json = json.dumps(to_json)
print("JSON string", now_json)
#now_json = json.dumps(to_json)

#print(now_json)