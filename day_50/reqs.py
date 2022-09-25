import requests

url="https://www.w3.org/TR/PNG/iso_8859-1.txt"

resp=requests.get(url)
c=resp.headers
print(c)
text=resp.text
print(text)
