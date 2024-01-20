while (True):
    n = int(input())
    divisor = []
    divisor_sum = 0
    
    if n == -1:
        break
    
    for j in range(1, n):
        if n % j == 0:
            divisor.append(j)
            divisor_sum += j
    
    if divisor_sum == n:
        print(n, "= ", end = "")
        
        for k in range(len(divisor)):
            print(divisor[k], end = "")
            
            if k != len(divisor) - 1:
                print(" + ", end = "")
            else:
                print()
    
    else:
        print(n, "is NOT perfect.")