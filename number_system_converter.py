def binary_to_decimal(n):
    
    n = int(n)
    power = 0
    result = 0
    
    while n > 0:
        
        r = n % 10
        result += r * (2 ** power) 
        power += 1
        n //= 10
        
    return result




def decimal_to_binary(n):
    
    n = int(n)
    res_str = ''
    
    while n > 1:
        
        r = n % 2
        res_str += str(r)
        n //= 2
        
    res_str += str(n)
    res_str = res_str[::-1]
    res = int(res_str)
    
    return res




def decimal_to_octal(n):
    
    n = int(n)
    res_str = ''
    
    while n > 7:
        
        r = n % 8
        res_str += str(r)
        n //= 8
        
    res_str += str(n)
    res_str = res_str[::-1]
    res = int(res_str)
    return res




def decimal_to_hexadecimal(n):
    
    n = int(n)
    res_str = ''
    
    while n > 15:
        
        r = n % 16
        if r == 10:
            res_str += 'A'
        elif r == 11:
            res_str += 'B'
        elif r == 12:
            res_str += 'C'
        elif r == 13:
            res_str += 'D'
        elif r == 14:
            res_str += 'E'
        elif r == 15:
            res_str += 'F'
        else:
            res_str += str(r)
        n //= 16
        
    res_str += str(n)
    res_str = res_str[::-1]
    
    return res_str




def hexadecimal_to_decimal(n):
    
    result = 0
    power = 0
    
    for x in n[::-1]:
        
        if x == 'A' or x == 'a':
            result += (16 ** power) * 10
        elif x == 'B' or x == 'b':
            result += (16 ** power) * 11
        elif x == 'C' or x == 'c':
            result += (16 ** power) * 12
        elif x == 'D' or x == 'd':
            result += (16 ** power) * 13
        elif x == 'E' or x == 'e':
            result += (16 ** power) * 14
        elif x == 'F' or x == 'f':
            result += (16 ** power) * 15
        else:
            result += (16 ** power) * int(x)
        power += 1
        
    return result




def octal_to_decimal(n):
    
    n = int(n)
    result = 0
    power = 0
    
    while n > 0:
        
        r = n % 10
        result += (8 ** power) * r
        n //= 10
        power += 1
        
    return result



def choices():    
    c1 = input('Which type of number you have ?\n1. B for Binary\n2. O for Octal\n3. D for Decimal\n4. H for Hexadecimal: ')
    c2 = input('Enter type you want to get:\n1. B for Binary\n2. O for Octal\n3. D for Decimal\n4. H for Hexadecimal: ')
    
    if c1 == 'B' or c1 == 'b':
        n = input('Enter your number you want to convert: ')
        
        if c2 == 'D' or c2 == 'd':
            return binary_to_decimal(n)
        elif c2 == 'O' or c2 == 'o':
            return decimal_to_octal(binary_to_decimal(n))
        elif c2 == 'H' or c2 == 'h':
            return decimal_to_hexadecimal(binary_to_decimal(n))
        elif c2 == 'B' or c2 == 'b':
            return n
        else:
            print('Invalid Choice !!\nSelect your choice....')
            choices()

        
        
    elif c1 == 'O' or c1 == 'o':
        n = input('Enter your number you want to convert: ')
        
        if c2 == 'B' or c2 == 'b':
            return decimal_to_binary(octal_to_decimal(n))
        elif c2 == 'O' or c2 == 'o':
            return n
        elif c2 == 'D' or c2 == 'd':
            return octal_to_decimal(n)
        elif c2 == 'H' or c2 == 'h':
            return decimal_to_hexadecimal(octal_to_decimal(n))
        else:
            print('Invalid Choice !!\nSelect your choice....')
            choices()
        
        
    elif c1 == 'D' or c1 == 'd':
        n = input('Enter your number you want to convert: ')
        
        if c2 == 'B' or c2 == 'b':
            return decimal_to_binary(n)
        elif c2 == 'D' or c2 == 'd':
            return n
        elif c2 == 'H' or c2 == 'h':
            return decimal_to_hexadecimal(n)
        else:
            print('Invalid Choice !!\nSelect your choice....')
            choices()
        
        
    elif c1 == 'H' or c1 == 'h':
        n = input('Enter your number you want to convert: ')
        
        if c2 == 'B' or c2 == 'b':
            return decimal_to_binary(hexadecimal_to_decimal(n))
        elif c2 == 'O' or c2 == 'o':
            return decimal_to_octal(hexadecimal_to_decimal(n))
        elif c2 == 'D' or c2 == 'd':
            return hexadecimal_to_decimal(n)
        elif c2 == 'H' or c2 == 'h':
            return n
        else:
            print('Invalid Choice !!\nSelect your choice....')
            choices()
    
    
    
    else:
        print('Invalid Choice !!\nSelect your choice....')
        choices()


print(f'Your desired number is: {choices()}')




'''


c1 = input('Which type of number you have ?\n1. B for Binary\n2. O for Octal\n3. D for Decimal\n4. H for Hexadecimal: ')
c2 = input('Enter type you want to get:\n1. B for Binary\n2. O for Octal\n3. D for Decimal\n4. H for Hexaecimal: ')
n = input('Enter your number you want to convert: ')


if c1 == 'B' or c1 == 'b':
     
    if c2 == 'D' or c2 == 'd':
        print(binary_to_decimal(n))
    elif c2 == 'O' or c2 == 'o':
        print(decimal_to_octal(binary_to_decimal(n)))
    elif c2 == 'H' or c2 == 'h':
        print(decimal_to_hexadecimal(binary_to_decimal(n)))
    elif c2 == 'B' or c2 == 'b':
        print(n)
    
        
        
elif c1 == 'O' or c1 == 'o':
        
    if c2 == 'B' or c2 == 'b':
        print(decimal_to_binary(octal_to_decimal(n)))
    elif c2 == 'O' or c2 == 'o':
        print(n)
    elif c2 == 'D' or c2 == 'd':
        print(octal_to_decimal(n))
    elif c2 == 'H' or c2 == 'h':
        print(decimal_to_hexadecimal(octal_to_decimal(n)))
    
        
        
elif c1 == 'D' or c1 == 'd':
        
    if c2 == 'B' or c2 == 'b':
        print(decimal_to_binary(n))
    elif c2 == 'D' or c2 == 'd':
        print(n)
    elif c2 == 'H' or c2 == 'h':
        print(decimal_to_hexadecimal(n))
    
        
        
elif c1 == 'H' or c1 == 'h':
        
    if c2 == 'B' or c2 == 'b':
        print(decimal_to_binary(hexadecimal_to_decimal(n)))
    elif c2 == 'O' or c2 == 'o':
         print(decimal_to_octal(hexadecimal_to_decimal(n)))
    elif c2 == 'D' or c2 == 'd':
        print(hexadecimal_to_decimal(n))
    elif c2 == 'H' or c2 == 'h':
        print(n)
        
'''