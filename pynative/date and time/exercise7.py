
from time import time

# time() function is multiplied with
# 1000 to convert seconds into milliseconds.
milliseconds = int(time() * 1000)

print(time())

print("Time in milliseconds since epoch", milliseconds)