list =[]
id_before = id(list)
n = int(input('enter the no. of items you want to add in the list: '))

for i in range(0,n):
    string = input('enter the string: ')
    list.append(string)

id_after = id(list)

#has the id of the list changed? 

if id_before == id_after:
    print('id of the list has not changed')
else:
    print('id of the list has changed')

# list sorting
sorted_list = sorted(list)
print('the sorted list is: ',sorted_list)

# first and second item
print('the first item on the list is ',sorted_list[0])
print('the second item on the list is ',sorted_list[1])