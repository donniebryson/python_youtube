
'''
JSON stands for JavaScript OBJECT Notation
JSON looks very similar to a python dictionary with the following exceptions:
JSON keys must be strings but python dictionary keys can be any immutable type
True in python becames true in JSON
False in python becomes false in JSON
None in python becomes null in JSON
JSON strings must have double quotes but dictionary strings can be double or single quote
The methods dump and dumps convert from a python dictionary to a JSON string
The methods load and loads convert from a JSON string to a python dictionary
'''
import json
# json.dumps takes a python dictionary and converts it to a JSON string
to_json = {"flag":True, "name":"donnie", "myblank": None}
print("dictionary", to_json)
now_json = json.dumps(to_json)
print("JSON string", now_json)
from_json = json.loads(now_json)
print("Data was JSON and now a dictionary -- ", from_json)
 

 