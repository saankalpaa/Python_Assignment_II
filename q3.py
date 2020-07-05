paragraph = input('enter a paragraph of text: ')
words= paragraph.split()
 
def findAnagram(words):
    dict = {}

    for word in words:
        key = ''.join(sorted(word))

        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)
                
        output= ''
        for key, value in dict.items():
            if len(value) > 1:
                output = output + ' '.join(value) + ' '

    return output  

print(findAnagram(words))