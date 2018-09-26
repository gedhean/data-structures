# -*- coding: utf-8 -*-

# Counting bits set (1)

# Gêdhean's way (naive)
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
# O(log(n))  Maybe the best 
def count_bit3(num):
    mask1 = 0b01010101 	# decimal 85
    mask2 = 0b00110011 	# decimal 51
    mask3 = 0b00001111 	# decimal 15

    num = (num & mask1) + ((num >> 1) & mask1) 
    num = (num & mask2) + ((num >> 2) & mask2)
    num = (num & mask3) + ((num >> 4) & mask3)
    return num

# Fastest and 'easy' way 
# Lookup in the array for the number of bits set 
def count_bit4(num):
	'''
	Return the number of bits set (1) for the given number (num)	
	'''	
	lookup = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,
 	2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,
 	4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1,2,
 	2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,
 	4,4,5,4,5,5,6,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,
 	3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,1,2,2,3,2,3,3,
 	4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,
 	5,6,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,
 	5,5,6,4,5,5,6,5,6,6,7,2,3,3,4,3,4,4,5,3,4,4,5,
 	4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,3,4,4,
 	5,4,5,5,6,4,5,5,6,5,6,6,7,4,5,5,6,5,6,6,7,5,6,
 	6,7,6,7,7,8]

 	return lookup[num]

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
