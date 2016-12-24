import os #imports methods and functions necessary to manipulate the system
currentDirectory = os.getcwd()
listOfItems = os.listdir(path=currentDirectory)
for item in listOfItems:
	nameSeparated = item.split()
	firstWord = nameSeparated[0]
	firstLetter = firstWord[0]
	if os.path.isdir('./' + str(firstLetter)) == True:
		os.rename((str(currentDirectory) + '/' + item), ((str(currentDirectory) + '/' + str(firstLetter) + '/' + item))
	else:
		os.mkdir('./' + str(firstLetter))
		os.rename((str(currentDirectory) + '/' + item), ((str(currentDirectory) + '/' + str(firstLetter) + '/' + item))
