import requests
import json
from io import BytesIO
import numpy as np

url = "http://localhost:8000"

# Data to be written, converted to bytes
data_arr = np.array([[1,2], [3,4],[5,6]])
original_shape = data_arr.shape
print("Original Array:\n", data_arr, "\n")
byte_arr = data_arr.tobytes()

x = ''
try:
    x = requests.post(url, data=byte_arr)
except requests.exceptions.ConnectionError:
    print("Connection refused")

'''
import numpy as np
from io import BytesIO
arr = np.array([[1,2], [3,4],[5,6]])
original_shape = arr.shape
print("Original Array:\n", arr, "\n")
byte_arr = arr.tobytes()
res = np.frombuffer(byte_arr, dtype=arr.dtype)
ans = res.reshape(original_shape)
print("Final Array:\n", ans, "\n")
'''