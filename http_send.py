import requests
import json


file_path = 'path/to/file.txt'
url = 'http://192.168.10.105:8080/api/get1'
#send_file(file_path, url)
data_dic={"name": "张三"}
response = requests.get(url, params=data_dic)
print(response.text)
