import os
from math import sqrt

def Divided(number, divisor):
	"""
	判断number是否可以被divisor整除
	"""
	if number%divisor == 0:
		return True
	else:
		return False

def LittlePrimeTest():
	"""
	测试一个数被小素数整除的概率
	"""
	flag2 = False
	flag3 = False
	flag5 = False
	flag7 = False
	flag11 = False
	flag13 = False
	flag17 = False
	flag19 = False

	divisor2 = 0
	divisor3 = 0
	divisor5 = 0
	divisor7 = 0
	divisor11 = 0

	divisor23 = 0
	divisor25 = 0
	divisor27 = 0
	divisor211 = 0
	divisor35 = 0
	divisor37 = 0
	divisor311 = 0
	divisor57 = 0
	divisor511 = 0
	divisor711 = 0

	divisor235 = 0
	divisor237 = 0
	divisor2311 = 0
	divisor257 = 0
	divisor2511 = 0
	divisor2711 = 0
	divisor357 = 0
	divisor3511 = 0
	divisor3711 = 0
	divisor5711 = 0

	divisor2357 = 0
	divisor23511 = 0
	divisor23711 = 0
	divisor25711 = 0
	divisor35711 = 0

	divisor235711 = 0

	divisor23571113 = 0
	divisor2357111317 = 0
	divisor235711131719 = 0


	for i in range(1,1000000000):
		flag2 = Divided(i, 2)
		flag3 = Divided(i, 3)
		flag5 = Divided(i, 5)
		flag7 = Divided(i, 7)
		flag11 = Divided(i, 11)
		flag13 = Divided(i, 13)
		flag17 = Divided(i, 17)
		flag19 = Divided(i, 19)

		if flag2 == True:
			divisor2 += 1
		if flag3 == True:
			divisor3 += 1
		if flag5 == True:
			divisor5 += 1
		if flag7 == True:
			divisor7 += 1
		if flag11 == True:
			divisor11 += 1
		
		if flag2 == True or flag3 == True:
			divisor23 += 1
		if flag2 == True or flag5 == True:
			divisor25 += 1
		if flag2 == True or flag7 == True:
			divisor27 += 1
		if flag2 == True or flag11 == True:
			divisor211 += 1
		if flag3 == True or flag5 == True:
			divisor35 += 1
		if flag3 == True or flag7 == True:
			divisor37 += 1
		if flag3 == True or flag11 == True:
			divisor311 += 1
		if flag5 == True or flag7 == True:
			divisor57 += 1
		if flag5 == True or flag11 == True:
			divisor511 += 1
		if flag7 == True or flag11 == True:
			divisor711 += 1

		if flag2 == True or flag3 == True or flag5 == True:
			divisor235 += 1
		if flag2 == True or flag3 == True or flag7 == True:
			divisor237 += 1
		if flag2 == True or flag3 == True or flag11 == True:
			divisor2311 += 1
		if flag2 == True or flag5 == True or flag7 == True:
			divisor257 += 1
		if flag2 == True or flag5 == True or flag11 == True:
			divisor2511 += 1
		if flag2 == True or flag7 == True or flag11 == True:
			divisor2711 += 1
		if flag3 == True or flag5 == True or flag7 == True:
			divisor357 += 1
		if flag3 == True or flag5 == True or flag11 == True:
			divisor3511 += 1
		if flag3 == True or flag7 == True or flag11 == True:
			divisor3711 += 1
		if flag5 == True or flag7 == True or flag11 == True:
			divisor5711 += 1

		if flag2 == True or flag3 == True or flag5 == True or flag7 == True:
			divisor2357 += 1
		if flag2 == True or flag3 == True or flag5 == True or flag11 == True:
			divisor23511 += 1
		if flag2 == True or flag3 == True or flag7 == True or flag11 == True:
			divisor23711 += 1
		if flag2 == True or flag5 == True or flag7 == True or flag11 == True:
			divisor25711 += 1
		if flag3 == True or flag5 == True or flag7 == True or flag11 == True:
			divisor35711 += 1

		if flag2 == True or flag3 == True \
		or flag5 == True or flag7 == True or flag11 == True:
			divisor235711 += 1
		if flag2 == True or flag3 == True \
		or flag5 == True or flag7 == True or flag11 == True \
		or flag13 == True:
			divisor23571113 += 1
		if flag2 == True or flag3 == True \
		or flag5 == True or flag7 == True or flag11 == True \
		or flag13 == True or flag17 == True:
			divisor2357111317 += 1
		if flag2 == True or flag3 == True \
		or flag5 == True or flag7 == True or flag11 == True \
		or flag13 == True or flag17 == True or flag19 == True:
			divisor235711131719 += 1

		if i%1000000 == 0:
			os.system("cls")
			print("="*50)
			print("在1~%d中，能够被下列小素数整数的数的比例为"%(i))
			print("by2 = %f"%(divisor2/i))
			print("by3 = %f"%(divisor3/i))
			print("by5 = %f"%(divisor5/i))
			print("by7 = %f"%(divisor7/i))
			print("by11 = %f"%(divisor11/i))

			print("by2or3 = %f"%(divisor23/i))
			print("by2or5 = %f"%(divisor25/i))
			print("by2or7 = %f"%(divisor27/i))
			print("by2or11 = %f"%(divisor211/i))
			print("by3or5 = %f"%(divisor35/i))
			print("by3or7 = %f"%(divisor37/i))
			print("by3or11 = %f"%(divisor311/i))
			print("by5or7 = %f"%(divisor57/i))
			print("by5or11 = %f"%(divisor511/i))
			print("by7or11 = %f"%(divisor711/i))

			print("by2or3or5 = %f"%(divisor235/i))
			print("by2or3or7 = %f"%(divisor237/i))
			print("by2or3or11 = %f"%(divisor2311/i))
			print("by2or5or7 = %f"%(divisor257/i))
			print("by2or5or11 = %f"%(divisor2511/i))
			print("by2or7or11 = %f"%(divisor2711/i))
			print("by3or5or7 = %f"%(divisor357/i))
			print("by3or5or11 = %f"%(divisor3511/i))
			print("by3or7or11 = %f"%(divisor3711/i))
			print("by5or7or11 = %f"%(divisor5711/i))

			print("by2or3or5or7 = %f"%(divisor2357/i))
			print("by2or3or5or11 = %f"%(divisor23511/i))
			print("by2or3or7or11 = %f"%(divisor23711/i))
			print("by2or5or7or11 = %f"%(divisor25711/i))
			print("by3or5or7or11 = %f"%(divisor35711/i))

			print("by2or3or5or7or11 = %f"%(divisor235711/i))
			print("by2or3or5or7or11or13 = %f"%(divisor23571113/i))
			print("by2or3or5or7or11or13or17 = %f"%(divisor2357111317/i))
			print("by2or3or5or7or11or13or17or19 = %f"%(divisor235711131719/i))


def IsPrime(num):
	endNum  = int(sqrt(num)+1)
	for i in range(2, endNum):
		if num%i == 0:
			return False
	return True

def ProbIter():
	prob = 0.5
	for pri in range(3, 1000000000):
		if IsPrime(pri):
			print(prob)
			prob = prob*(pri-1)/pri+1/pri;


def main():
	#LittlePrimeTest()
	ProbIter()


if __name__ == '__main__':
	main()


