import os

filePath = input("Enter the file path (ex. users/kyle/python/ :")
if os.path.isdir(filePath):
    print('Directory Exists')
fileName = input('Enter the file name:')
userName = input('Enter your name: ')
userAddress = input('Enter your address: ')
userPhone = input('Enter your phone number: ')
f = open(fileName, 'w')
f.write(userName + ',' + userAddress + ',' + userPhone)
f.close()
readFile = open(fileName, 'r')
data = readFile.read()
print(data)
readFile.close()






