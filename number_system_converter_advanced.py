def anything_to_decimal(any_number_system, n):
    
    result = 0
    power = 0
    
    if any_number_system == 16:
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
        return int(result)
    
    else:
        n = int(n)
        while n > 0:
            r = n % 10
            result += r * (any_number_system ** power)
            power += 1
            n //= 10
        
        return result





def converter(desired_number_system, entered_number_converted_to_decimal):
    if desired_number_system == 16:
        #entered_number_converted_to_decimal = int(entered_number_converted_to_decimal)
        res_str = ''
        while entered_number_converted_to_decimal > 15:
            r = entered_number_converted_to_decimal % 16
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
            entered_number_converted_to_decimal //= 16
        res_str += str(entered_number_converted_to_decimal)
        res_str = res_str[::-1]
        
        return res_str
    else:
        #n = int(n)
        res_str = ''
        desired_number_system = int(desired_number_system)
        while entered_number_converted_to_decimal > (desired_number_system-1):
            
            r = entered_number_converted_to_decimal % desired_number_system
            res_str = res_str + str(r) 
            entered_number_converted_to_decimal //= desired_number_system
            
        res_str += str(entered_number_converted_to_decimal)
        res_str = res_str[::-1]
        #res = int(res_str)
        
        return res_str




def main():
    
    any_number_system = int(input('Enter current base of number: '))

    desired_number_system = int(input('Enter base you want to convert:  '))

    n = input(f'Please enter a number you want to convert from base {any_number_system} to base {desired_number_system} : ')
    
    print(f'Your number {n} converted to base {desired_number_system} is: ', end='--->  ')
    print(converter(desired_number_system, entered_number_converted_to_decimal = anything_to_decimal(any_number_system, n)))

main()