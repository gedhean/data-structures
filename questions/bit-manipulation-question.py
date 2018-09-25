#!/user/bin/python
# -*- coding: utf-8 -*-

# Counting bits set (1)

# Gêdhean's way
def bits_set1(num):
	'''Return the number of bits set (1) for the given number (num)'''
	count = 0
	for bit in bin(num):
		if bit == '1':
			count += 1
	return count

# Brian Kernighan's way
def bits_set2(num):
	'''Return the number of bits set (1) for the given number (num)'''
	count = 0
	while num:
		num = num & (num - 1)
		count += 1
	return count

# Function to count the number of bits that are 
# different between two numbers
def diff_bits(num1, num2):
	'''Return the number of different bits between two numbers (num1 and num2)'''
	diffs = num1 ^ num2
	return bits_set2(diffs)

if __name__ == '__main__':
	print('Number of bits one in number 1:', bits_set1(1))
	print('Number of bits one in number 3:', bits_set1(3))
	print('Number of bits one in number 1:', bits_set2(1))
	print('Number of bits one in number 3:', bits_set2(3))
	print('Number of different bits between 2 and 3:', diff_bits(2,3))
