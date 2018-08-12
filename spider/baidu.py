'''import urllib.request

response = urllib.request.urlopen("https://www.baidu.com")
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader("Server"))
print(response.read().decode("utf-8"))
'''
from urllib import request, parse

url = "http://httpbin.org/post"
headers = {
    # 伪装一个火狐浏览器
    "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "host": 'httpbin.org'
}
dict = {
    "name": "Germey"
}
data = bytes(parse.urlencode(dict), encoding="utf8")
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))