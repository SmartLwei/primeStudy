"""
欧几里得算法
求两个数的最大公约数
原理为：
gcd(a,b) = gcd(b, a(mod b))
"""

import os
import sys
	
def Eclid(a,b):
	"""
	欧几里得算法
	求两个数的最大公约数
	"""
	if b==0:
		return a
	return Eclid(b, a%b)

def main():
	if len(sys.argv) != 3:
		print("请输入两个整数")
		a = int(input("a="))
		b = int(input("b="))
	else:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	res = Eclid(a, b)
	print("gcd(%d,%d)=%d"%(a,b,res))


if __name__ == '__main__':
	main()
	os.system("pause")