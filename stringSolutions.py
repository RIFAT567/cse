# s = list(input())
# sentence = input()
# a = s.copy()
# a[0] = s[-1]
# a[-1] = s[0]
# print("".join(a))

# b = list()
# for i in range(len(s)-1):
#     b.append(s[i+1])
# b.append(s[0])
# print("".join(b))

# c = s[::-1]
# print("".join(c))

# d = list(s[i] for i in range(len(s)) if i%2!=0)
# print("".join(d))

# e = list(s[i] for i in range(len(s)) if i%2==0)
# print("".join(e))

# f = [s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))]
# print("".join(f))

# vowels = "AEIOUaeiou"
# g = [x for x in s if x in vowels]
# print("".join(g))

# h = [x for x in s if x not in vowels]
# print("".join(h))

# i = [x for x in s if x in vowels]
# i.reverse()
# print("".join(i))

# j = [x for x in s if x not in vowels]
# j.reverse()
# print("".join(j))

# k = [x for x in s if x.isupper()]
# k.reverse()
# print("".join(k))

# l = [x for x in s if x.islower()]
# l.reverse()
# print("".join(l))

# m = [x for x in s if x.islower()]
# n = [x for x in s if not x.islower()]
# print("".join(m + n))

# o = [i.islower() for i in s]
# print("LOWERCASE: ", sum(o))
# print("UPPERCASE: ", len(o) - sum(o))

# # 1.15
# p = [int(x) for x in s if x.isnumeric()]
# print(sum(p))

# # 1.16
# q = [i.isalpha() for i in s]
# r = [i.isnumeric() for i in s]
# print("CHARS: ", sum(q))
# print("DIGITS: ", sum(r))
# print("SYMBOLS: ", len(s) - sum(q) - sum(r))

# 1.17
# current_char = s[0]
# current_count = 1
# longest_char = s[0]
# longest_count = 1

# for char in s[1:]:
#     if char==current_char:
#         current_count += 1
#     else:
#         current_char = char
#         current_count = 1
#     if current_count > longest_count:
#         longest_count = current_count
#         longest_char = current_char
# print(longest_char, longest_count)

# s_copy = [x for x in s if x.isnumeric()]
# print("".join(s_copy))

# t = [x.upper() for x in s if x.isalpha()]
# print("".join(t))

# u = [x for i, x in enumerate(s) if x not in s[:i]]
# print("".join(u))
# sentence = input()
# word_counts = {}
# for x in sentence.split():
#     key = x.casefold()
#     if key in word_counts:
#         word_counts[key][1] += 1
#     else:
#         word_counts[key] = [x, 1]
# for word, count in word_counts.values():
#     print(f"{word}: {count}")
    
# print(sentence.title())

# changed_sentence = []
# for char in s:
#     if char == "Z":
#         changed_sentence.append("A")
#     elif char == "z":
#         changed_sentence.append("a")
#     elif char.isalpha():
#         changed_sentence.append(chr(ord(char) + 1))
#     else:
#         changed_sentence.append(char)
# print("".join(changed_sentence))

# dnas = list(map(list, input().split()))
# hd = [i==j for i, j in zip(dnas[0], dnas[1])]
# print(len(hd) - sum(hd))

# pattern = list(input().strip().upper())
# complement = {
# 	"A": "T",
# 	"T": "A",
# 	"C": "G",
# 	"G": "C"
# }

# complemented = [complement[code] for code in pattern]
# complemented.reverse()
# print("".join(complemented))

# s = input().split(" ")
# for i in range(len(s)):
# 	s[i] = "".join(reversed(s[i]))
# print(" ".join(s))

# dict = {}
# s = input()
# set = set(s.strip())
# print(sorted(set))
# for i in sorted(set):
#     dict[i] = s.count(i)
# for key, value in dict.items():
# 	print(f"{key}: {value}")
 
# s = input()
# vow = dict((x, s.count(x)) for x in s if x in "AEIOUaeiou")
# print(sorted(vow))
# for vowels in sorted(vow):
#     print(f"{vowels}: {vow[vowels]}")

# Largest word(s) in a line
# words = input().split()

# max_length = max(len(word) for word in words)
# longest_words = [word for word in words if len(word) == max_length]
# print(" ".join(longest_words))

# s1 = input().split()
# s2 = input().split()

# merged = [s1[i]+s2[i] for i in range(len(s1))]
# print(" ".join(merged))

# s = input()
# print(s.swapcase())

# s = input()

# for i in range(len(s)):
#     print(s[:i+1])

# s = input()

# result = []
# current_char = s[0]
# char_count = 1

# for char in s[1:]:
#     if char == current_char:
#         char_count += 1
#     else:
#         result.append(current_char + str(char_count))
#         current_char = char
#         char_count = 1

# result.append(current_char + str(char_count))
# print("".join(result))

# s = input()
# substrings = []
# substring = []
# for chr in s:
#     if chr in substring:
#         substrings.append("".join(substring))
#         substring.clear()
#         substring.append(chr)
#     else:
#         substring.append(chr)

# print(max(substrings, key=len))

# s1 = sorted(input().lower())
# s2 = sorted(input().lower())

# if s1 == s2:
#     print("True")
# else:
#     print("False")

# s = input().split()
# palindromes = [word for word in s if len(word) > 1 and word == word[::-1]]
# print("\n".join(palindromes))

# s = input().split()
# pl = [word[1:] + word[0] + "ay" if word[0] not in "aeiouAEIOU" else word + "way" for word in s]
# print(" ".join(pl))

# 1.39
# s = input().split()
# print(" ".join(s[::-1]))

# s = input()
# max_count = 0
# max_char = ""

# for x in s:
#     if s.count(x) > max_count:
#         max_count = s.count(x)
#         max_char = x
#     else:
#         pass
# print(max_char, max_count)

# s = list(input())
# k = int(input())
# cipher = []
# for x in s:
#     if x.isalpha():
#         if x.isupper():
#             if ord(x)+k > 90:
#                 cipher.append(chr(ord(x)+k-26))
#             else:
#                 cipher.append(chr(ord(x)+k))
#         else:
#             if ord(x)+k > 122:
#                 cipher.append(chr(ord(x)+k-26))
#             else:
#                 cipher.append(chr(ord(x)+k))
#     else:
#         cipher.append(x)
# print("".join(cipher))

# text = input()
# matching_brackets = {
# 	")": "(",
# 	"]": "[",
# 	"}": "{",
# }
# stack = []
# valid = True

# for character in text:
# 	if character in "([{":
# 		stack.append(character)
# 	elif character in matching_brackets:
# 		if not stack or stack.pop() != matching_brackets[character]:
# 			valid = False
# 			break

# print(valid and not stack)

# 1.43
# s = input().split()
# anagram_pairs = []

# for first_index in range(len(s)):
#     for second_index in range(first_index + 1, len(s)):
#         if sorted(s[first_index]) == sorted(s[second_index]):
#             anagram_pairs.append([s[first_index], s[second_index]])

# if not anagram_pairs:
#     print("None")
# for pair in anagram_pairs:
#     print(" ".join(pair))
        
# s = input().split()
# first_letters = [x[0] for x in s]
# vowel = [letter in "AEIOUaeiou" for letter in first_letters]
# consonent = [letter not in "AEIOUaeiou" for letter in first_letters]
# print(f"Vowel-start: {sum(vowel)}")
# print(f"Vowel-start: {sum(consonent)}")

# s = input()
# n = int(input())
# if n < len(s):
#     print(s[:n] + "...")
# else:
#     print(s)

# s = input().split()
# prefix = []

# min_word = min(s, key=len)
# for i in range(1, len(min_word)+1):
#     if all(word.startswith(min_word[0:i]) for word in s):
#         prefix.append(min_word[0:i])
#     else:
#         break
# if prefix:
#     print(prefix[-1])
# else:
#     print("None")

# s = input().lower().split()
# words = [
# 	"".join(character for character in word if character.isalnum())
# 	for word in s
# ]
# print("_".join(words))

# expression = input()
# result = 0
# current_number = 0
# operator = "+"
# for character in expression:
#     if character.isnumeric():
#         current_number = current_number * 10 + int(character)
#     elif character in "+-":
#         if operator=="+":
#             result+=current_number
#         else:
#             result-=current_number
#         operator = character
#         current_number = 0
# if operator=="+":
#     result+=current_number
# else:
#     result-=current_number
# print(result)

# s = input()
# if len(s) > 4:
#     print((len(s)-4) * "*" + s[-4:])
# else:
#     print(s)

# s = input()
# phrase = []
# for x in s:
#     if x.isalnum():
#         phrase.append(x.lower())
# if phrase == phrase[::-1]:
#     print("True")
# else:
#     print("False")

s = input().split()
vow = "aeiouAEIOU"
print(" ".join(x[::-1] for x in s))
print(" ".join(x for x in s if x.isalpha() and x[0] not in vow and x[-1] not in vow))
