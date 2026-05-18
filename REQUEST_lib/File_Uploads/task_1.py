import requests

url = "https://httpbin.org/post"

files = {
    'file' : open(r"C:\Users\PranavMangal\Desktop\Python my work deep dive\REQUEST_lib\File_Uploads\sample.txt", "rb")
}

response = requests.post(url, files=files)

print(response.json())