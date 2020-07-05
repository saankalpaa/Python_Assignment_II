my_name = ('Sankalpa', 'Pokhrel', 22)

list = []

list.append(my_name)

friend_1 = ('Shreya', 'Baidya', 23)

friend_2 = ('Aviseck', 'Rauniyar', None)

list.append(friend_1)
list.append(friend_2)

age = []
for i in range (len(list)):
    if list[i][2]:
        age.append(list[i][2])

average_age = sum(age)/len(list)

for i in range (len(list)):
    name = list[i][0] + ' ' + list[i][1]
    if list[i][2]:
        if list[i][2] > average_age:
            print(name + ' ' + 'is old!!')
        else:
            print(name + ' ' + 'is young!!')
    else:
        print(name + ' ' + 'has no age!!')
