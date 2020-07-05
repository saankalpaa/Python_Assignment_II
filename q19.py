class validity:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return 'not valid'
        return 'valid'


v = validity()
print(v.is_valid_parenthese("(){}[]"))
print(v.is_valid_parenthese("({[)]"))
print(v.is_valid_parenthese("{{{"))