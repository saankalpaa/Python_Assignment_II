def change_case(str,separator): 
    result = [str[0].lower()] 
    for i in str[1:]: 
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            result.append(separator) 
            result.append(i.lower()) 
        else: 
            result.append(i) 
      
    return ''.join(result) 
     
str = "ThisIsCamelCased"
print(change_case(str,'_')) 
print(change_case(str,'-'))