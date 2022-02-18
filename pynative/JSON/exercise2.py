

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2

#value2
json_object = json.loads(sampleJson)
print(json_object["key2"])