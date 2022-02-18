from __future__ import print_function
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary
#7000
y = json.loads(sampleJson)
print(y["company"]["employee"]["payble"]["salary"])





