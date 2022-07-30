# nvir-mask-demo

This is a demo repo to demonstrate [nilvana vision inference runtime](https://nilvana.tw/products/nilvana-vision-inference-runtime).

Please refer to the medium [article](https://medium.com/hello-nilvana/%E9%80%8F%E9%81%8E-nilvana-vision-inference-runtime-%E9%83%A8%E7%BD%B2%E6%A8%A1%E5%9E%8B-a52b05a63b74). 👈👈👈👈👈👈

## Get Started ##

```shell
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

python3 simple.py   # image request
python3 simple2.py --url='http://127.0.0.1:52010/v1/infer/111111111' --image='assets/demo.jpg' # with display
python3 video.py --url='http://127.0.0.1:52010/v1/infer/111111111' --video='assets/demo.mp4'   # video
```

## Demo

| ![image](output/demo.png) |
|:--:|
| <b>Image with bounding boxes</b>|

| ![image](output/demo.gif) |
|:--:|
| <b>Video with bounding boxes</b>|


## Assets

- Video by cottonbro from Pexels: https://www.pexels.com/video/woman-art-iphone-smartphone-3960181/

- Photo by cottonbro from Pexels: https://www.pexels.com/photo/people-wearing-face-mask-for-protection-3957986/