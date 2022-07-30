import requests
import json

url = 'http://127.0.0.1:52010/v1/infer/111111111' # change this!

# inference
files = {'image': open('assets/demo.jpg', 'rb')}
response = requests.post(url, files=files)
result = json.loads(response.text)
print(result)
