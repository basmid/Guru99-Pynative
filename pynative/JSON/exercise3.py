
import json

Json_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
# {
#   "key1" = "value2",
#   "key2" = "value2",
#   "key3" = "value3"
# }

str_JSON = json.dumps(Json_dict, indent=2, separators=(","," = "))
print(str_JSON)



