def digitNum(n,arr):
    if(n<=0):
        return 1;
    digit = int(n%10)
    n = int(n/10)
    ans = digitNum(n,arr)
    print(arr[digit])
    return ans
    
if __name__ == "__main__":
    n = 42457
    arr=["zero","one","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    ans = digitNum(n,arr)