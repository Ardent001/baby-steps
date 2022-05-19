import request as kind

url = input('Webpage to grab source from: ')

req = kind.get(url)

print(req.text)
