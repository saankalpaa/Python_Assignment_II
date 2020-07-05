list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]


def enter_data_in_file(list):
    file = open("data.csv", "w")
    file.write('name,address,age \n')
    for i in range(len(list)):
        item = tuple(map(str, list[i]))
        row = ','.join(item)
        file.write(row + '\n')

    file.close()


enter_data_in_file(list)