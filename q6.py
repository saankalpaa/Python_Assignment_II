list =[]
n = int(input('enter the no. of items you want to add in the list: '))

for i in range(0,n):
    names = input('enter the name of your friend or colleague: ')
    list.append(names)

string=''

for i in list:
    if 'john' in list:
        string = 'john'
        
    else:
        string ='not found'
        
print(string)

