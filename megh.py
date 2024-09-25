def fib(n):
     if n<=1:
        return n
     f=[0,1]
     for i in range(2,n+1):
        f.append(f[i-1]+[i-2])
        print("the fibonacci sequence is",f)
        print("the fibonacci value is :",fib(n))