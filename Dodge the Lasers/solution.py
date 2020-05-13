#python3 code

import math

def soln(num):
    # Based on Beatty's numbers. This is a cool math trick. 
    if (num == 0):
      return 0

    sqrt = "414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831"
    
    n = num
    n_prime = str(int(sqrt) * n)[:-156]
    if len(n_prime) == 0:
      n_prime = 0
    else:
      n_prime = int(n_prime)
    
    return (n_prime + n) * (n_prime + n + 1) / 2 - n_prime * (n_prime + 1) - soln(n_prime)



def solution(s):
    #your source code
    return str(int(soln(int(s))))
