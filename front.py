#!/usr/bin/python3
import requests

print("Content-Type: text/html",  end="\r\n\r\n", flush=True)
print("<html>")
print("<head>")
print("<title>Jokes!</title>")
print("</head>")
print("<body>")
print("")

jokerequest = requests.get("https://example.com/jsonAPI")
jokedata = jokerequest.json()
try:
        joke = jokedata["text"]
        print(joke)
except KeyError:
        print("There was a KeyError")


print("</body>")
print("</html>")
