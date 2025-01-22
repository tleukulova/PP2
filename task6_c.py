p=lambda x:all(x % i!=0 for i in range(2,int(x**0.5)+1)) and x>1
n=input()
num=[int(nu) for nu in n.split()]
prime=list(filter(p,num))

print(prime)