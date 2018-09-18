from http.client import HTTPConnection
conn = HTTPConnection("google.com")

conn.request("GET", "/")
result = conn.getresponse()

content = result.read()
print(content)