def powerFunc(x,n):
    if(n==0):
        return 1
    if(n%2!=0):  #for odd power values
        ans = x * powerFunc(x,int(n-1))
        return ans
    elif(n%2==0):  #for even power values
        ans = powerFunc(x * x ,int(n/2))
        return ans
        
if __name__ == "__main__":
    n = 3
    x = 2
    if(n<0):
        ans = powerFunc(x,abs(n))
        print(1/ans)
    else:
        ans = powerFunc(x,n)
        print(ans)
