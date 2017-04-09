import xmlrpc.client
item = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(item.system.listMethods())
print(item.system.methodHelp('phone'))
print(item.phone('Bert'))

print('http://www.pythonchallenge.com/pc/return/italy.html')
