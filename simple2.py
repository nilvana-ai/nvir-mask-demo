import requests
import json
import cv2

url = 'http://192.168.41.200:52010/v1/infer/111111111' # change this!

# inference
img = cv2.imread('./assets/demo.jpg')
_, img_encoded = cv2.imencode('.jpg', img)
files = {'image': ('image.jpg', img_encoded.tobytes(), 'image/jpeg')}
response = requests.post(url, files=files)
result = json.loads(response.text)

# draw bounding boxes on the image
for obj in result['result']:
    obj_name = obj['label']
    x1, y1, x2, y2 = int(obj['xmin']), int(obj['ymin']), int(obj['xmin']+obj['width']), int(obj['ymin']+obj['height'])

    label = "{}: {:.2f}%".format(obj_name, obj['confidence'] * 100)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    img = cv2.putText(img, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imshow('demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()