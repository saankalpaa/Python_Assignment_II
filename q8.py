num = int(input('enter the number: '))

def is_prime(num):
    if num > 1:
        count = 0
        for i in range(1,num):
            if (num % i) == 0:
                count = count + 1
            else:
                pass
        print(count)
        if count < 2:
            return True
        else:
            return False

print(is_prime(num))

