"""
生成素数
用于其他的模块
"""
from math import sqrt

prime = [2]

def TestPrime(num):
	endNum  = int(sqrt(num)+1)
	for i in range(2, endNum):
		if num%i == 0:
			return False
	return True

def main():
	global prime
	for i in range(3, 10000):
		if TestPrime(i):
			prime.append(i)

main()

if __name__ == '__main__':
	print(prime)