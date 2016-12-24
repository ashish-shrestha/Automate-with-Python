import os #imports methods and functions necessary to manipulate the system
currentDirectory = os.getcwd() #creates a variable currentDirectory in which the currentDirectory path is stored
listOfItems = os.listdir(path=currentDirectory) #creates a list of all items in current directory
for item in listOfItems: #looping over each item in current directory
	firstLetter = item[0] #grabs first letter to determine where item will be placed
	firstLetter = firstLetter.upper() #shifts letter to uppercase to avoid separation of items like 'python' and 'Python' (case-sensitive)
	if os.path.isdir(str(currentDirectory) + '/' + str(firstLetter)) == True: #if directory already exists...
		os.rename((str(currentDirectory) + '/' + item), (str(currentDirectory) + '/' + str(firstLetter) + '/' + item)) #simply move the file/folder
	else: #if directory doesn't exist
		os.mkdir(str(currentDirectory) + '/' + str(firstLetter)) #make the directory
		os.rename((str(currentDirectory) + '/' + item), (str(currentDirectory) + '/' + str(firstLetter) + '/' + item)) #and then move the file/folder

