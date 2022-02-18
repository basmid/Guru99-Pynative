#mijn versie
import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }

sortedJson = json.dumps(sampleJson, indent=4, sort_keys=True)
print(sortedJson)
jsonFile = open("data.json", "w")
jsonFile.write(sortedJson)
jsonFile.close()

#site versie
# import json
#
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
#
# print("Started writing JSON data into a file")
# with open("sampleJson.json", "w") as write_file:
#     json.dump(sampleJson, write_file, indent=4, sort_keys=True)
# print("Done writing JSON data into a file")