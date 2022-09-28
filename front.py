#!/usr/bin/python3
import requests

print("Content-Type: text/html",  end="\r\n\r\n", flush=True)
print("<html>")
print("<head>")
print("<title>Title</title>")
print("</head>")
print("<body>")
print("")

requestdata = requests.get("https://example.com/jsonAPI")
datajson = requestdata.json()
try:
        data = datajson["text"]
        print(data)
except KeyError:
        print("There was a KeyError")


print("</body>")
print("</html>")
