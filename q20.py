array = [-25, -10, -7, -3, 2, 4, 8, 10]
n= len(array)

class Sum:
    def sum_to_zero(self, array, n):
        result = []
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (array[i] + array[j] + array[k] == 0):
                        result.append([array[i], array[j], array[k]])
        return result

print(Sum().sum_to_zero(array,n))