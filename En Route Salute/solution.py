#python3 code

def count(i,s):
    ans=0
    for j in range(i,len(s)):
        if(s[j]=="<"):
            ans+=1
    return ans
    
def higher(s):
    res=0
    for i in range(len(s)):
        if(s[i]==">"):
            b=count(i,s)
            res=res+(b*2)
    return res
    
def solution(s):
    # Your code here
    result=higher(s)
    return result
