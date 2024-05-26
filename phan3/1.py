num = int(input("Input a number: "))
def myFunc(x):
    n = x - 17
    ans = 0
    if n >= 0:  
        ans = n * 2
    else: 
        ans = abs(n)
    return ans
print(myFunc(num))