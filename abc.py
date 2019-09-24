with open('abc.txt','r+') as file:
    a = file.read()
    a = a*5
    file.write(a)
    print(a)