#print("Hello World")

'''
items = 'zero one two three'.split()
print(items)
#공백으로 분류
'''

'''
example = 'python,jquary,javascript'
print(example.split(","))
# , 로 분류
'''

'''
example = 'cs.aaa.edu'
subdomain , domain, tld = example.split(".")
print(subdomain,domain,tld)
# . 으로 각각의 변수에 분류
'''

'''
word_1 = ["hello","you","are"]
word_2 = ["world","is","big"]
result = [i+" "+j for i in word_1 for j in word_2]
print(result)
# 각각의 인자와 합하기
'''

'''
word_1 = ["hello","you","are"]
word_2 = ["world","is","big"]
result = [i+" "+j for i in word_1 for j in word_2 if not(i==j)]
print(result)
#중복제거
'''

'''
word_1 = ["hello","you","are"]
word_2 = ["world","is","big"]
result = [[i+" "+j for i in word_1 if not(i==j)] for j in word_2]
print(result)
#2차원 배열로
'''

'''
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist,blist):
    print(a,b)
# 같은 인덱스끼리 묶음
'''

'''
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
print([sum(x) for x in zip((1,2,3,),(10,20,30),(100,200,300))])
# 같은 튜플끼리 묶음
'''

'''
result = {i:j for i,j in enumerate('Hi my name is mino'.split())}
print(result)
#딕셔너리로 분리후 인덱싱
'''

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
