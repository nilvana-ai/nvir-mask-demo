import cv2
import numpy as np
import requests
import json
from imutils.video import FileVideoStream
import imutils

url = 'http://192.168.41.200:52010/v1/infer/111111111' # change this 

def get_color(label):
    """helper function"""
    if label == "mask":
        return (0, 255, 0)
    return (0, 0, 255)

fvs = FileVideoStream('assets/demo.mp4').start()

while fvs.more():
    frame = fvs.read()
    if frame is not None:
        # resize frame
        frame = imutils.resize(frame, width=1024)

        # inference
        _, img_encoded = cv2.imencode('.jpg', frame)
        files = {'image': ('image.jpg', img_encoded.tobytes(), 'image/jpeg')}
        response = requests.post(url, files=files)
        result = json.loads(response.text)

        # draw bbox on the frame
        for obj in result['result']:
            if obj['confidence'] > 0.95:
                obj_name = obj['label']
                color = get_color(obj_name)
                x1, y1, x2, y2 = int(obj['xmin']), int(obj['ymin']), int(obj['xmin']+obj['width']), int(obj['ymin']+obj['height'])

                label = "{}: {:.2f}%".format(obj_name, obj['confidence'] * 100)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                frame = cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # display
        cv2.imshow('demo', frame)

        # exit with q button
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# sanitize
cv2.destroyAllWindows()
fvs.stop()