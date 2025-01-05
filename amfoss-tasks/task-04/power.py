def sum(X, N,num=1):
    
    power = num ** N
    
    if power > X:
        return 0

    if power == X:
        return 1

    include = sum(X - power, N, num + 1)
    exclude = sum(X, N, num + 1)
    
  
    return include+ exclude

X = int(input())
N = int(input())
result = sum(X, N)
print(result)
