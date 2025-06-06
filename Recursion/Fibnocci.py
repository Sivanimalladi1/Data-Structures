def myfunc(n):
    if(n==1):
        return 1
    if(n==0):
        return 0
    ans = myfunc(n-1) + myfunc(n-2)
    return ans
        
if __name__ == "__main__":
    n=4
    ans = myfunc(n)
    print(ans)