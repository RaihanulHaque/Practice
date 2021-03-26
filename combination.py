def split(string):
	return list(string)

def combination(string):
	alphabets = split(string)
	list = []
	for i in alphabets:
		for j in alphabets:
			for k in alphabets:
				for l in alphabets:
					result = i+j+k+l
					list.append(result)
	return list
				
string = input('Enter the text to create combination: ')
list = combination(string)
with open("CombinationList.txt", "w+") as file:
	for item in range (0,len(list)):
		file.write(list[item])
		file.write("\t\n")
count = 0
for i in list:
	count = count+1
print("Total Combination is: ",count)