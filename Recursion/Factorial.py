def factorial(n):
    if(n==0):
        return 1
   
    ans = n * factorial(n-1) 
    return ans
        
if __name__ == "__main__":
    n=4
    ans = factorial(n)
    print(ans)