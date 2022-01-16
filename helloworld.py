a="Hello World"
print(a)

a="Life is too short   \n You need python"

b = """ I am hungry
Let's go eat dinner"""
print(a)
print(type(a))

print(b)



#인덱싱은 0부터 시작한다 슬라이싱은 [시작:끝:간격]
print(a[0])
print(a[:8:-2])


c = "I eat %d apples." %3
print(c)

# %d는 정수 %f는 실수 %s는 문자열 사실 %s 로 쓰면 다 됨
number=10
day="three"
a = "I ate %d apples. so I was sick for %s days." %(number,day)

print(a)

a= "my name is {name}. I am {age} years old.".format(name="홍상명",age=24)
print(a)

#0.4f 하면 소숫점 아래 4자리까지 출력
a = "%0.4f" % 3.42132434

print(a)

a = "hobby"
print(a.count("b"))

print(a.find("b"))

1844

a = "," .join("abcd")
print(a)

print(a.upper())

a = "Life is too short"
print(a.replace("Life","Your leg"))

#리스트 : 변수 여러 개를 묶는 역할
a = ["이시영","문재성","김정현",["홍상명","홍준형"]]
print(a[3])

a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)

a = ["박주하","잠수","문재성"]
#a[0:2]는 0에서 2 미만이라는 뜻, 즉 1번째에서 3번째 미만
a[0:2] = ["한재성","홍상명"]
print(a)

del a[0]

a.append("시우버")
print(a)

a = [1,5,3]
a.reverse()

#0번째 인덱스에 4를 추가해라
a = [1,5,3]
a.insert(0,4)
print(a.index(3))

print(a.pop())

print(a.count(1))

print(a.extend([2,3]))
print(a)

t1 = (1,2,'a','b')

print(t1)
t2 = (3,4)

print(t1+t2)

print(t1*3)

#딕셔너리 {}

dic = {'name' : 'Eric', 'age' : 15}

print(dic['name'])

a = {1: 'a'}
a['name']="익명"

print(a)

del a[1]
print(a)

a = {1: 'a', 2: 'b'}
print(a)

a = {1: '파랑구름', 2: '이현준', 3: '민MIN준JUN'}
print(a)

print(a.keys())
print(a.values())

#튜플 형태로 쌍 담음
print(a.items())

for k in a.items() : 
    print(k)
    
#a라는 딕셔너리에 4가 없으면 '없음' 출력
print(a.get(4,'없음'))

#true 나 false로 출력해줌
print(4 in a)
