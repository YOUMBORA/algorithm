def solution(N, number):
    
    n = 1
    N_dict = {}
    multiply_number = N

    for i in range(1,9):
        N_dict[i] = [multiply_number]
        if multiply_number == number:
            return i
        multiply_number *= 10
        multiply_number += N
        
    while n <= 8:
        for i in range(1,n//2+1):
            last, first = i, n-i
            for j in N_dict[last]:
                for k in N_dict[first]:
                    temp_list = [j+k, j-k, j*k, k-j]
                    if k!=0 and j!=0:
                        temp_list.extend([j//k, k//j])
                        
                    if number in temp_list:
                        return n
                    else:
                        N_dict[n].extend(temp_list)
        N_dict[n] = list(set(N_dict[n]))
        n+=1

    return -1
