import request as kind

url_input = input('Webpage to grab source from: ')
url_output = input('Name for html file: ')

req = kind.get(url, 'html.parser')

with open(url_output, 'w') as url:
    url.write(req.text)
    url.close()
