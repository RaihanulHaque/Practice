def combination(list, prev, text, n):
    if len(prev) == n:
        list.append(prev)
        return
    for i in range(len(text)):
        combination(list, prev + [text[i]], text, n)
        
text = list(input('Enter the text to make combination: '))
n = int(input('Enter the length of text which you want to see: '))
list = []
answer= []

combination(list, [], text, n)
for x in range(0,len(list)):
    temp = ''.join(list[x])
    answer.append(temp)

with open("CombinationList.txt", "w+") as file:
	for item in range (0,len(answer)):
		file.write(answer[item])
		file.write("\n")
print(len(answer))
print(answer)