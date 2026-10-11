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

with open("input.txt") as input:
    data = input.readlines()
    list1 = data[0].strip().split()
    list2 = data[1].strip().split()
    for i,j in zip(list1,list2):
        print(i,j)
    