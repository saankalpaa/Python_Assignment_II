my_name = ('Sankalpa', 'Pokhrel', 22)

list = []

list.append(my_name)

friend_1 = ('Shreya', 'Baidya', 23)

friend_2 = ('Aviseck', 'Rauniyar', 26)

list.append(friend_1)
list.append(friend_2)

sorted_list = sorted(list, key = lambda first_name: first_name[0])
print('sorted by first name: ',sorted_list)

sorted_list = sorted(list, key = lambda last_name: last_name[1])
print('sorted by last name: ',sorted_list)

sorted_list = sorted(list, key = lambda age: age[2])
print('sorted by age: ',sorted_list)