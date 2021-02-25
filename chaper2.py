import sys, os


## 1
print(r'C:\Window\notepad.exe')


##2
FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGLE']

for idx, symbol in enumerate(FAANG, 1): # 1 : 인덱스 시작값
    print(idx, symbol)

##3
i = 1
while i < 7:
    print(i)
    i += 2
else:
    print("Done")

##4
L = [1,2]
L.extend([3,4]) #  반복 자료형일 때, 내부 원소를 추가
print(L)

##CAGR - Compound Annual Growth Rates 연평균 성장률
def getCAGR(first, last, years):
    return (last/first)**(1/years)-1
cagr = getCAGR(65300, 2669000, 20)
print("SEC CAGR : {:2%}".format(cagr))

