#!python
print("content-type: text/html; charset=utf-8")
print()#\n역할

import cgi,os

files = os.listdir('data')
# print(files)
listSTR = ''
for item in files:
    listSTR = listSTR + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
# print(listSTR)

form = cgi.FieldStorage()

if 'id' in form :
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    # description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello Web'
# print(pageId)

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <!--<li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>-->
    {listSTR}
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc = description, listSTR = listSTR))
