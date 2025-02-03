# Finding the Middle Element in a List

numList = [1, 2, 3, 4, 5]
midElement = int((len(numList)/2))

print(numList[midElement])

# Converting a List into a String

lst = ["P", "Y", "T", "H", "O", "N"]
string = ''.join(lst)

print(string)
print(type(string))

# Adding Two List Elements Together

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

res_lst = []
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i])
print(res_lst)