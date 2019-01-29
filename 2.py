'''
def f(x,y):
    return x+y

print(f(1,4))


f = lambda x,y : x+y
print(f(1,4))

f = lambda x : x **2
print(f(2))

f = lambda x : x/2
print(f(3))

print( (lambda x : x+1) (5))
#lambda 함수 응용
#간단한 함수만들기
'''

'''
ex = [1,2,3,4,5]
f = lambda x: x**2
print(list(map(f,ex)))

f = lambda x,y : x+y
print(list(map(f,ex,ex)))

list(map(lambda x:x**2 if x%2==0 else x, ex))
#map func
#모든 인자에 대해서 각각의 함수를 실행
'''

'''
from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))
(((1+2)+3)+4)+5 = 15

def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
((((1*2)*3)*4)*5) = 120
print(factorial(5))
#reduce func 모든 값에대해 한번씩 실행
'''
