import requests


def upload_file():
    url = "https://httpbin.org/post"
    
    files = {
        "file": open(r"C:\Users\PranavMangal\Desktop\Python my work deep dive\REQUEST_lib\File_Uploads\sample.txt", "rb")
    }
    
    data = {
        "user_id" : "123",
        "doc_type": "resume"
    }
    
    res = requests.post(url, files=files, data = data)
    
    print(res.json())
    return res

def download_file():
    url = "https://httpbin.org/image/png"
    
    res = requests.get(url, stream=True)
    
    with open("download.png", "wb")as f:
        for chunks in res.iter_content(1024):
            f.write(chunks)
    
    return res

