import requests

url = "http://127.0.0.1:5000/detect-image"

image_url = "https://imgs.search.brave.com/wIvxhq2vN-1zyZEqvx-Ll6inr_Vx8YK8gFDbNb8Q7As/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTgy/NDI5NzA0L3Bob3Rv/L3JlY3ljbGFibGUt/c29ydGluZy1jb252/ZXlvci13aXRoLWNh/bnMtYW5kLXBsYXN0/aWMuanBnP3M9NjEy/eDYxMiZ3PTAmaz0y/MCZjPWFseDBfaElY/TFlrQUdQVnQyRG81/bkF2RjFPQVlQX0xY/Vk1XTHZnNlVWVEU9"

img = requests.get(image_url).content

files = {"image": ("image.jpg", img)}

response = requests.post(url, files=files)

print(response.json())