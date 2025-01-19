# pip install requests
import requests
res = requests.get('http://127.0.0.1:8080')
# res = requests.get('http://127.0.0.1:8080/pages/hello.html')
print(res.text)
