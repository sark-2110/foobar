#python3 code

def solution(l):
    # Your code here
    triples = 0
    c= [0] * len(l)
    for i in range(0,len(l)):
        j=0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                triples += c[j]
    return triples
