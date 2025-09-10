import requests
import json

url = "http://192.168.2.26:8848/ocr"
payload = json.dumps({"image_path": "/home/qzq/图片/res.png"})
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=payload)
result = response.json()
print(json.dumps(result, ensure_ascii=False, indent=2))
