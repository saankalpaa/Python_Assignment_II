string = input('enter the string: ')

def is_palindrome(string):
    reversed_string = ''.join(reversed(string))
    if reversed_string == string:
        print('palindrome')
    else:
        print('not palindrome')

is_palindrome(string)