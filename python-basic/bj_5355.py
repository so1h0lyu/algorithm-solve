t = int(input())

while t > 0:
    case = input().split()
    number = float(case[0])
    l = len(case)
    
    for i in range(1, l):
        operator = case[i]
        
        if (operator == '@'):
            number *= 3
        elif (operator == '%'):
            number += 5
        elif (operator == '#'):
            number -= 7
    
    print("{:.2f}".format(number))
    t -= 1