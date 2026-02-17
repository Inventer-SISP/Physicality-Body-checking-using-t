file = open('atu','r')
print(file.read())
file.close()

file = open('atu','r')
print("\n read 1 line")
print(file.readlines())
file.close()

file = open('atu','r')
print("\n read 3 line")
print(file.readlines())
print(file.readlines())
print(file.readlines())

file = open('atu','r')

print("\n read this")
for line in file:
    print (line)
file.close()