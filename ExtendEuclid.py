"""
扩展的欧几里得算法
计算a·x+b·y = d = gcd(a,b)中的x和y

迭代关系
r(-1)=a				x(-1)=1 				y(-1) = 0
r(0)=b 				x(0)=0					y(0)=1
循环下面的迭代关系
r(i)=r(i-2)%r(i-1)	x(i)=x(i-2)-q(i)x(i-1)	y(i)=y(i-2)-q(i)y(i-1)
q(i)=r(i-2)/r(i-1)
if(r(i)==0) break

例如
a=1759, b=550
i		r(i)	q(i)	x(i)	y(i)
-1		1759			1		0
0		550				0		1
1		109		3		1		-3
2		5		5		-5		16
3		4		21		106		-339
4		1		1		-111	355
5		0		4		end		end
因此 1759*-111+550*355=1
如果需要求 550的逆元(mod 1759),根据上面的等式
550*355 mod 1759 = 1, 因此550模1759的乘法逆元是355
"""

import os
import sys

def ExtendEuclid(a,b):
	#迭代的初始值
	r_2 = a
	r_1 = b
	x_2 = 1
	x_1 = 0
	y_2 = 0
	y_1 = 1
	r = b
	x = 0
	y = 1
	#利用上面公式进行迭代求值
	while True:
		r = r_2%r_1
		#结束的条件
		if(r == 0):
			return r_1,x,y
		q = r_2//r_1
		x = x_2 - q*x_1
		y = y_2 - q*y_1
		#每轮迭代后更新状态值
		r_2 = r_1
		r_1 = r
		x_2 = x_1
		x_1 = x
		y_2 = y_1
		y_1 = y
		#调试用
		#print("r =",a*x+b*y)
	pass
	
def main():
	if len(sys.argv) != 3:
		print("请输入两个整数")
		a = int(input("a="))
		b = int(input("b="))
	else:
		a = int(sys.argv[1])
		b = int(sys.argv[2])

	if a<b:
		temp = a
		a = b
		b = temp
	ret = ExtendEuclid(a, b)
	print(ret)
	if ret[0] == 1:
		print("%d^-1 (mod %d) = %d"%(b, a, ret[2]))

if __name__ == '__main__':
	main()

