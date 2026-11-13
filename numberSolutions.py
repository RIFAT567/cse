# num = int(input())
# binary_num = bin(num)[2:]  # Convert to binary and remove the '0b' prefix
# octal_num = oct(num)[2:]   # Convert to octal and remove the '0o' prefix
# hexadecimal_num = hex(num)[2:]  # Convert to hexadecimal and remove the '0x' prefix
# print(f"Binary: {binary_num}")
# print(f"Octal: {octal_num}")
# print(f"Hexadecimal: {hexadecimal_num}")

# # Write a program that prompts the user to input two numbers and display its HCF. The Highest Common Factor (HCF) also called the Greatest Common Divisor (GCD) of two whole numbers, is the largest whole number that’s a factor of both of them.

# def find_hcf(x, y):
#     while(y):
#         x, y = y, x % y
#     return abs(x)
# num1 = int(input())
# num2 = int(input())
# print(find_hcf(num1, num2))

# Write a program that asks the user for a positive integer value. The program should calculate the sum of all the integers from 1 up to the number entered. For example, if the user enters 20, the loop will find the sum of 1, 2, 3, 4, … 20.

# num = int(input())
# result = 0
# for i in range(1, num+1):
#     result+=i
# print(result)

# Write a program that asks the user to input a positive integer. Your program should find and display the sum of digits of number. For example, sum of digits of number 32518 is 3+2+5+1+8 = 19

# n = list(map(int, input()))
# print(sum(n))

# Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number. A prime number is a number that is evenly divisible only by itself and 1. For example, the number 5 is prime because it can be evenly divided only by 1 and 5. The number 6, however, is not prime because it can be divided evenly by I, 2, 3, and 6.

# n = int(input())
# 
# if n > 1:
#     is_prime = True
#     for i in range(2, n):
#         if n%i==0:
#             is_prime = False
#         else:
#             continue
# print(is_prime)

# Write a program that prompts the user to input a positive integer and print sum of all prime numbers less than or equal to that number. For example, if the user enters 10, the program should calculate the sum of 2, 3, 5, and 7, which is 17.

# n = int(input())
# primes = []
# is_prime = False
# for i in range(1, n):
#     if i > 1:
#         is_prime = True
#         for j in range(2, i):
#             if i%j==0:
#                 is_prime = False
#             else:
#                 continue
#     if is_prime:
#         primes.append(i)
# print(sum(primes))

# Write a program that prompts the user to input a positive integer and check whether it is an Armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371

# n = list(map(int, input()))
# digits = [i**3 for i in n]
# if str(sum(digits)) == "".join(map(str, n)):
#     print("Armstrong")
# else:
#     print("Not Armstrong")
    
# Write a program that prompts the user to input a positive integer. It should then output the factorial of that number. Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720

# n = int(input())
# result = 1
# for i in range(1, n+1):
#     result*=i
# print(result)

# Write a Python program that prompts the user to input a positive integer and checks if a number is a “Strong Number”. A Strong number is a special number whose sum of the factorial of digits is equal to the original number. For example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145.

# n = list(map(int, input()))
# facts = []
# result = 1
# for i in n:
#     for j in range(1, i+1):
#         result*=j
#     facts.append(result)
#     result = 1
# if str(sum(facts)) == "".join(map(str, n)):
#     print("Strong number")
# else:
#     print("Not strong number")

# Write a Python program that prompts the user to input a positive integer and checks if a number is a “Harshad Number” (also called a Niven number). A Harshad number is an integer that is divisible by the sum of its digits. For example, 18 is a Harshad number because 1 + 8 = 9 and 18 is divisible by 9.

# n = list(map(int, input()))
# if int("".join(map(str, n)))%sum(n)==0:
#     print(True)
# else:
#     print(False)

# Write a Python program that prompts the user to input a positive integer and check if a number is an “Automorphic Number”. A number is called automorphic if its square ends in the same digits as the number itself. For example, 252 = 625 (ends in 25) and 762 = 5776 (ends in 76)
# n = int(input())
# count = len(str(n))
# if str(n*n)[-count:] == str(n):
#     print("Automorphic number")
# else:
#     print("Not automorphic number")

# Write a Python program that prompts the user to input a positive integer and checks if a number is a “Disarium Number”. A number is called Disarium if the sum of its digits raised to the power of their respective positions is equal to the number itself. For example: 135 = 11 + 32 + 53
# n = input()
# dis = [int(j)**(i+1) for i,j in (enumerate(n))]
# if sum(dis) == int(n):
#     print("Disarium number")
# else:
#     print("Not disarium number")

# Write a Python program that prompts the user to input a positive integer number and print the Grade Letter.
# marks = int(input())
# grade = ""
# if marks >= 0 and marks <= 100:
#     if marks >= 80:
#         grade = "A+"
#     if marks >= 70 and marks < 80:
#         grade = "A"
#     if marks >= 60 and marks < 70:
#         grade = "A-"
#     if marks >= 50 and marks < 60:
#         grade = "B"
#     if marks >= 40 and marks < 50:
#         grade = "C"
#     if marks < 40:
#         grade = "F"
#     print(grade)
# else:
#     print("Wrong number")

# Given two numerical values find out the relationship between them First line of the input file is an integer t (t < 15) which denotes how many sets of inputs are there. Each of the next t lines contain two integers a and b. For each line of input produce one line of output. This line contains any one of the relational operators ‘>’, ‘<’ or ‘=’, which indicates the relation that is appropriate for the given two numbers.

# with open("input.txt") as file:
#     data = file.readlines()
# cnt = int(data[0].strip())
# current = []
# rltn = []
# for i in data[1:cnt+1]:
#     current = i.strip().split()
#     if current[0] > current[1]:
#         rltn.append(">")
#     elif current[0] == current[1]:
#         rltn.append("=")
#     else:
#         rltn.append("<")
# with open("output.txt", "w") as output:
#     output.write("\n".join(rltn))

# Write a Python program that takes a list of integers from user and print all the integers in reverse order

# n = input().split()
# print(" ".join(n[::-1]))

# Write a Python program that takes a list of integers from user and print square of all the integers.

# n = input().split()
# m = [str(int(i)**2) for i in n]
# print(" ".join(m))

# Write a Python program that takes two list of integers from user and print integers from list1 in original order and integers from list2 in reverse order.

# with open("input.txt") as input:
#     data = input.readlines()
#     list1 = data[0].strip().split()
#     list2 = data[1].strip().split()
#     for i,j in zip(list1,reversed(list2)):
#         print(i,j)
    
# Write a Python program that takes a list of integers from user and print all the odd & even integers in ascending order separately.

# n = map(int, input().split())
# even = list()
# odd = list()
# for num in n:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print(f'even: {" ".join(map(str, sorted(even)))}')
# print(f'odd: {" ".join(map(str, sorted(odd)))}')

# Write a Python program that takes two list of integers from user in two line and print all the common integers between those two list in ascending order.

# with open("input.txt") as input_file:
#     data = input_file.readlines()
#     set1 = set(map(int, data[0].split()))
#     set2 = set(map(int, data[1].split()))
#     result = sorted(set1.intersection(set2))
#     print(*result)

# Write a Python program that takes two list of integers from user in two line and print all the pairwise difference between those two list in ascending order.

# set1 = list(map(int, input().strip().split()))
# set2 = list(map(int, input().strip().split()))
# print(set1)
# print(set2)
# differences = []
# for i,j in zip(set1, set2):
#     print(f'difference of {i} and {j}', abs(i-j))
#     differences.append(abs(i-j))
# differences.sort()
# print(*differences)

# Write a Python program that takes multi line of input from user where each line contains space separted list of integers. Your program should combine all the integer numbers and print them in descending order.

# with open("input.txt") as file:
#     lines = [line.split() for line in file]

# numbers = [int(number) for line in lines for number in line]
# numbers.sort(reverse=True)
# print(*numbers)

# Write a Python program that takes a list of integers from user. Your program print out sum, max, min and avg of all integers.

# n = list(map(int, input().split()))
# print(f"sum: {sum(n)}")
# print(f"max: {max(n)}")
# print(f"min: {min(n)}")
# print(f"avg: {sum(n)/len(n)}")

# Write a Python program that takes a list of integers from user. Your program should count all the unique integers and print them in ascending order by their frequency.

# n = list(map(int, input().split()))
# dict = {i:n.count(i) for i in n}
# sorted_dict = sorted(dict.items(), key=lambda x: x[1])
# for key, value in sorted_dict:
#     print(f"{key}: {value}")

# Write a Python program that takes a list of integers from user. Your program should count all the unique pair of integers and print them in ascending order by their frequency.

# from collections import Counter

# n = list(map(int, input().split()))
# pair_counts = Counter(zip(n, n[1:]))
# sorted_pairs = sorted(pair_counts.items(), key=lambda item: item[1])
# for key, value in sorted_pairs:
#     print(*key, value)

# Write a Python program that takes a list of integers from user. Your program print out sum, max, min and avg of all odd integers and even integers separately.

# n = list(map(int, input().split()))
# even = [i for i in n if i%2==0]
# odd = [i for i in n if i%2!=0]
# print(f'sum (even): {sum(even)}')
# print(f'sum (odd): {sum(odd)}')
# print(f'max (even): {max(even)}')
# print(f'max (odd): {max(odd)}')
# print(f'min (even): {min(even)}')
# print(f'min (odd): {min(odd)}')
# print(f'avg (even): {sum(even)/len(even)}')
# print(f'avg (odd): {sum(odd)/len(odd)}')

# Write a Python program that takes two numbers 𝑛, 𝑚 and a list of 𝑛𝑋𝑚 integers from user in a single line. Your program print out those integers as a 𝑛𝑋𝑚 matrix.

# with open("input.txt") as input:
#     data = input.readlines()
#     n,m = map(int, data[0].strip().split())
#     nums = data[1].strip().split()
#     print(nums)
#     row = 0
#     for i in range(n):
#         for j in range(m):
#             print(nums[row+i+j], end=" ")
#         row+=4
#         print()

# Write a Python program that takes a matrix (𝑛𝑋𝑚 where 𝑛 lines and each line has 𝑚 integer numbers) as input. Your program should print out the transpose of that matrix.

# with open("input.txt") as input:
#     data = input.readlines()
#     init_matrix = [data[i].strip().split() for i in range(len(data))]
#     col_num = len(init_matrix)
#     matrix = [
#         [init_matrix[j][i] for j in range(col_num)] for i in range(len(init_matrix[0]))
#     ]
#     for i in range(len(matrix)):
#         for j in matrix[i]:
#             print(j, end=" ")
#         print()

# Write a Python program that takes a list of integers from user in a single line. Your program print out all possible pair wise combination between those integers.

# set = list(map(int, input().split()))
# pairs = list()
# index = 0
# for num in set:
#     for i in set[index+1:]:
#         pairs.append([str(num), str(i)])
#     index+=1
# print(pairs)
# for pair in pairs:
#     print(" ".join(pair))

# Write a Python program that takes a list of integers from user in a single line. Your program print out all possible pair wise permutation between those integers.

# with open("input.txt") as input:
#     data = input.read()
#     print(data)
#     set = list(data.split())
#     pairs = list()
#     print(set)
#     for num in set:
#         for i in set:
#             if num==i:
#                 continue
#             else:
#                 pairs.append([num, i])
#     for pair in pairs:
#         print(" ".join(pair))

# Write a Python program that takes a list of integers from user. Your program print out the integers which  occurred only once in the list.

# numbers = list(map(int, input().split()))
# num_count = {x:numbers.count(x) for x in numbers}
# print(num_count)
# ones = [str(key) for key in num_count.keys() if num_count[key]==1]
# print(" ".join(ones))

# Given an integer x, return true if x is a palindrome, and false otherwise.

# num = input()
# if num == num[::-1]:
#     print("true")
# else:
#     print("false")

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it. Explanation: For example, given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.